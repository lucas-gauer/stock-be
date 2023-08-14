from source.database import get_db
from source.models.user import CreateUser
from .user import UserRepository

db = next(get_db())


def test_create():
    product = CreateUser(name="John Doe", password="Str0ngPass!")
    created_product = UserRepository.create(db, product)

    assert created_product.name == product.name
    assert created_product.password == product.password


def test_exists():
    id_to_find = 1
    product_exists = UserRepository.exists(db, id_to_find)

    assert product_exists


def test_find_many():
    products = UserRepository.find_many(db)

    assert len(products) > 0


def test_find_one():
    id_to_find = 1
    product = UserRepository.find_one(db, id_to_find)

    assert product
    assert product.user_id == id_to_find

def test_find_one_by_name():
    name_to_find = "John Doe"
    product = UserRepository.find_one_by_name(db, name_to_find)

    assert product
    assert product.name == name_to_find


def test_update_one():
    id_to_update = 1
    user = CreateUser(name="John Doe", password="An0therStr0ngPass!")
    updated_user = UserRepository.update_one(db, id_to_update, user)

    assert updated_user
    assert updated_user.name == user.name
    assert updated_user.password == user.password


def test_delete_one():
    id_to_delete = 1
    deleted_id = UserRepository.delete_one(db, id_to_delete)

    assert deleted_id
    assert deleted_id == id_to_delete
