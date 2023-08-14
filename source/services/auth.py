from datetime import datetime, timedelta
from fastapi import Header
from sqlalchemy.orm import Session

from jose import JWTError, jwt

from source.constants import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from source.exceptions import jwt_exception, login_exception
from source.repositories.user import UserRepository


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = datetime.utcnow() + expire_delta

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def validate_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise jwt_exception from None

    return payload


def login(db: Session, username: str, password: str) -> dict:
    db_user = UserRepository.find_one_by_name(db, username)
    if db_user is None:
        raise login_exception

    if db_user.password != password:
        raise login_exception

    return {"access_token": create_access_token({"user_id": db_user.user_id})}


def get_current_user(Authorization: str = Header(..., description="JWT key")):
    return validate_access_token(Authorization[7:])
