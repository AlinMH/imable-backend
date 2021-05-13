import os

from fastapi import Depends, FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from sqlalchemy.orm import Session

from .database.session import database, user_db
from .deps import db_session
from .models.education import Education as EducationModel
from .models.experience import Experience as ExperienceModel
from .schemas.education import Education as EducationSchema
from .schemas.education import EducationDB
from .schemas.experience import Experience as ExperienceSchema
from .schemas.experience import ExperienceDB
from .schemas.user import User, UserCreate, UserDB, UserUpdate

APP_SECRET = os.getenv("APP_SECRET")

jwt_authentication = JWTAuthentication(secret=APP_SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login")

app = FastAPI()
fastapi_users = FastAPIUsers(
    user_db,
    [jwt_authentication],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
app.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_reset_password_router(APP_SECRET), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_verify_router(APP_SECRET), prefix="/auth", tags=["auth"])
app.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/user/experience", tags=["experience"], response_model=list[ExperienceDB])
def get_user_experience(user: User = Depends(fastapi_users.current_user()), session: Session = Depends(db_session)):
    experiences = session.query(ExperienceModel).filter(ExperienceModel.user_id == user.id).all()
    return [
        ExperienceDB(
            id=exp.id,
            position=exp.position,
            employer=exp.employer,
            city=exp.city,
            start_date=exp.start_date,
            end_date=exp.end_date,
            description=exp.description,
        )
        for exp in experiences
    ]


@app.post("/user/experience", tags=["experience"], status_code=status.HTTP_201_CREATED)
def add_user_experience(
    request: ExperienceSchema,
    user: User = Depends(fastapi_users.current_user()),
    session: Session = Depends(db_session),
):
    experience = ExperienceModel(**request.dict(), user_id=user.id)
    session.add(experience)
    session.commit()
    session.refresh(experience)


@app.put("/user/experience", tags=["experience"])
def edit_user_experience(
    id: int,
    request: ExperienceSchema,
    response: Response,
    user: User = Depends(fastapi_users.current_user()),
    session: Session = Depends(db_session),
):
    experience = (
        session.query(ExperienceModel)
        .filter(ExperienceModel.user_id == user.id)
        .filter(ExperienceModel.id == id)
        .one_or_none()
    )
    if experience:
        experience.position = request.position
        experience.employer = request.employer
        experience.city = request.city
        experience.start_date = request.start_date
        experience.end_date = request.end_date
        experience.description = request.description
        session.commit()
        session.refresh(experience)
        return

    response.status_code = status.HTTP_404_NOT_FOUND


@app.delete("/user/experience", tags=["experience"])
def remove_user_experience(
    id: int,
    response: Response,
    user: User = Depends(fastapi_users.current_user()),
    session: Session = Depends(db_session),
):
    deleted = (
        session.query(ExperienceModel)
        .filter(ExperienceModel.user_id == user.id)
        .filter(ExperienceModel.id == id)
        .delete()
    )

    if not deleted:
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    session.commit()


@app.get("/user/education", tags=["education"], response_model=list[EducationDB])
def get_user_education(user: User = Depends(fastapi_users.current_user()), session: Session = Depends(db_session)):
    educations = session.query(EducationModel).filter(EducationModel.user_id == user.id).all()
    return [
        EducationDB(
            id=edu.id,
            edu_type=edu.edu_type.value,
            name=edu.name,
            city=edu.city,
            start_date=edu.start_date,
            end_date=edu.end_date,
        )
        for edu in educations
    ]


@app.post("/user/education", tags=["education"], status_code=status.HTTP_201_CREATED)
def add_user_education(
    request: EducationSchema,
    user: User = Depends(fastapi_users.current_user()),
    session: Session = Depends(db_session),
):
    edu = EducationModel(**request.dict(), user_id=user.id)
    session.add(edu)
    session.commit()
    session.refresh(edu)


@app.put("/user/education", tags=["education"])
def edit_user_education(
    id: int,
    request: EducationSchema,
    response: Response,
    user: User = Depends(fastapi_users.current_user()),
    session: Session = Depends(db_session),
):
    education = (
        session.query(EducationModel)
        .filter(EducationModel.user_id == user.id)
        .filter(EducationModel.id == id)
        .one_or_none()
    )
    if education:
        education.edu_type = request.edu_type
        education.name = request.name
        education.city = request.city
        education.start_date = request.start_date
        education.end_date = request.end_date
        session.commit()
        session.refresh(education)
        return

    response.status_code = status.HTTP_404_NOT_FOUND


@app.delete("/user/education", tags=["education"])
def remove_user_education(
    id: int,
    response: Response,
    user: User = Depends(fastapi_users.current_user()),
    session: Session = Depends(db_session),
):
    deleted = (
        session.query(EducationModel).filter(EducationModel.user_id == user.id).filter(EducationModel.id == id).delete()
    )

    if not deleted:
        response.status_code = status.HTTP_404_NOT_FOUND
        return

    session.commit()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
