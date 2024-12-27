from pydantic import BaseModel


class CreatedUserModel(BaseModel):
    email: str
    name: str
    nickname: str
    avatar_url: str
    uuid: str
