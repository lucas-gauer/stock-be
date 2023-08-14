from pydantic import BaseModel

class CreateUser(BaseModel):
    name: str
    password: str

class User(CreateUser):
    user_id: int
