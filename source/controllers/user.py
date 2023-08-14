from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from source.database import get_db

from source.models.user import CreateUser, User
from source.repositories.user import UserRepository


router = APIRouter(prefix="/user")


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create(request: CreateUser, db: Session = Depends(get_db)):
    return UserRepository.create(db, request)
