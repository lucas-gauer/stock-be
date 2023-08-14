from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    stock: int


class Product(CreateProduct):
    product_id: int
