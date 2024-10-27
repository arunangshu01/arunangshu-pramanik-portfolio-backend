from pydantic import BaseModel, ValidationInfo, HttpUrl, field_validator, EmailStr
import re


class SocialMediaProfiles(BaseModel):
    linkedin: HttpUrl
    github: HttpUrl
    leetcode: HttpUrl


class Location(BaseModel):
    city: str
    state: str
    country: str

    @field_validator('*')
    @classmethod
    def validate_location_fields(cls, value: str, field_info: ValidationInfo) -> str:
        if not 2 < len(value) <= 50:
            raise ValueError(f"{field_info.field_name} is not within proper length size.")
        return value


class PersonalInformation(BaseModel):
    name: str
    phone: str
    location: Location
    email: EmailStr
    social_media_profiles: SocialMediaProfiles

    @field_validator('name')
    @classmethod
    def validate_name(cls, value: str, field_info: ValidationInfo) -> str:
        if ' ' not in value:
            raise ValueError(f"No Space Present in {field_info.field_name}.")
        return value.title()

    @field_validator('phone')
    @classmethod
    def validate_phone_number(cls, value: str, field_info: ValidationInfo) -> str:
        phone_number_pattern = r"\+91-\d{5}-\d{5}"
        phone_number_match = re.match(phone_number_pattern, value)
        if not phone_number_match:
            raise ValueError(f"Invalid {field_info.field_name}.")
        return value


