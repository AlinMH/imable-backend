from datetime import date
from typing import Optional

from fastapi_users import models
from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    format_number,
    is_valid_number,
    number_type,
)
from phonenumbers import parse as parse_phone_number
from pydantic import constr, validator


class User(models.BaseUser):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: constr(max_length=50, strip_whitespace=True) = None
    location: Optional[str] = None
    birthdate: Optional[date] = None

    @validator("phone_number")
    def check_phone_number(cls, v):
        if v is None:
            return v
        try:
            n = parse_phone_number(v, "RO")
        except NumberParseException as e:
            raise ValueError("Please provide a valid mobile phone number") from e

        if not is_valid_number(n) or number_type(n) not in (
            PhoneNumberType.MOBILE,
            PhoneNumberType.FIXED_LINE_OR_MOBILE,
        ):
            raise ValueError("Please provide a valid mobile phone number")

        return format_number(n, PhoneNumberFormat.NATIONAL if n.country_code == 44 else PhoneNumberFormat.INTERNATIONAL)


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
