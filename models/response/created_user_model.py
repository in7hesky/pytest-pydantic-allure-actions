from pydantic import BaseModel, field_validator, ValidationError


class CreatedUserModel(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: str

    @field_validator("email", "name", "nickname", "uuid")
    @classmethod
    def field_not_empty(cls, field):
        if field is None or field == "":
            raise ValidationError("Field is empty")

    @field_validator("avatar_url")
    @classmethod
    def field_empty(cls, field):
        if field is not None and field != "":
            raise ValidationError("Field is not empty")
