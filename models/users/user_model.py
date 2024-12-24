from pydantic import BaseModel, field_validator


class UserModel(BaseModel):
    email: str
    name: str
    nickname: str
    uuid: str

    @field_validator("*")
    @classmethod
    def check_field_not_empty(cls, field):
        if field == "" or field is None:
            raise ValueError("Field is empty")
