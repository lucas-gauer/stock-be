from source.database import get_db
from source.models.product import CreateProduct
from .product import ProductRepository

db = next(get_db())


def test_create():
    product = CreateProduct(name="Product 1", stock=10)
    created_product = ProductRepository.create(db, product)

    assert created_product.name == product.name
    assert created_product.stock == product.stock


def test_exists():
    id_to_find = 1
    product_exists = ProductRepository.exists(db, id_to_find)

    assert product_exists


def test_find_many():
    products = ProductRepository.find_many(db)

    assert len(products) > 0


def test_find_one():
    id_to_find = 1
    product = ProductRepository.find_one(db, id_to_find)

    assert product
    assert product.product_id == id_to_find


def test_update_one():
    id_to_update = 1
    product = CreateProduct(name="Product One", stock=5)
    updated_product = ProductRepository.update_one(db, id_to_update, product)

    assert updated_product
    assert updated_product.name == product.name
    assert updated_product.stock == product.stock


def test_delete_one():
    id_to_delete = 1
    deleted_id = ProductRepository.delete_one(db, id_to_delete)

    assert deleted_id
    assert deleted_id == id_to_delete
