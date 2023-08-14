from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from source.database import get_db
from source.models.product import CreateProduct, Product
from source.repositories.product import ProductRepository
from source.services.auth import get_current_user

router = APIRouter(prefix="/product")


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create(
    request: CreateProduct,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    return ProductRepository.create(db, request)


@router.get("/", response_model=list[Product])
def find_many(
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    return ProductRepository.find_many(db)


@router.get("/{id}", response_model=Product)
def find_one(
    id: int,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    product = ProductRepository.find_one(db, id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )

    return product


@router.put("/{id}", response_model=Product)
def update_one(
    id: int,
    request: CreateProduct,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    if not ProductRepository.exists(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )

    return ProductRepository.update_one(db, id, request)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one(
    id: int,
    db: Session = Depends(get_db),
    _user: dict = Depends(get_current_user),
):
    if not ProductRepository.exists(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado",
        )
    ProductRepository.delete_one(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
