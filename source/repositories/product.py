from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from source.models.product import CreateProduct, Product


class ProductRepository:
    @staticmethod
    def create(db: Session, product: CreateProduct) -> Product:
        results = db.execute(
            text(
                f"""INSERT INTO products (name, stock) VALUES ("{product.name}", {product.stock}) RETURNING *"""
            )
        )
        db.commit()

        return Product(**results.mappings().one())

    @staticmethod
    def exists(db: Session, id: int) -> bool:
        results = db.execute(text(f"SELECT * FROM products WHERE product_id='{id}'"))

        return results.first() is not None

    @staticmethod
    def find_many(db: Session) -> list[Product]:
        results = db.execute(text("SELECT * FROM products"))

        return [Product(**product) for product in results.mappings().all()]

    @staticmethod
    def find_one(db: Session, id: int) -> Product | None:
        results = db.execute(text(f"SELECT * FROM products WHERE product_id={id}"))

        product = results.mappings().first()

        return Product(**product) if product else None

    @staticmethod
    def update_one(db: Session, id: int, product: CreateProduct) -> Product | None:
        db.execute(
            text(
                f"UPDATE products SET name='{product.name}', stock={product.stock} WHERE product_id={id}"
            )
        )
        db.commit()

        return Product(product_id=id, **product.model_dump())

    @staticmethod
    def delete_one(db: Session, id: int) -> int | None:
        results = db.execute(
            text(f"DELETE FROM products WHERE product_id={id} RETURNING product_id")
        )
        db.commit()

        deleted_id = results.first()

        return deleted_id[0] if deleted_id else None
