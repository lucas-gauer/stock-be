from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from source.database import get_db
from source.models.auth import Login, Token
from source.services import auth as AuthService

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=Token, status_code=status.HTTP_201_CREATED)
def login(request: Login, db: Session = Depends(get_db)):
    return AuthService.login(db, request.name, request.password)
