from pydantic import BaseModel


class AccessTokenContent(BaseModel):
    user_id: int


class Token(BaseModel):
    access_token: str


class Login(BaseModel):
    name: str
    password: str
