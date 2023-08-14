from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from source.models.user import CreateUser, User

# TODO password hashing


class UserRepository:
    @staticmethod
    def create(db: Session, user: CreateUser) -> User:
        results = db.execute(
            text(
                f"""INSERT INTO users (name, password) VALUES
                ("{user.name}", "{user.password}") RETURNING *"""
            )
        )
        db.commit()

        return User(**results.mappings().one())

    @staticmethod
    def exists(db: Session, id: int) -> bool:
        results = db.execute(text(f"SELECT * FROM users WHERE user_id='{id}'"))

        return results.first() is not None

    @staticmethod
    def find_many(db: Session) -> list[User]:
        results = db.execute(text("SELECT * FROM users"))

        return [User(**user) for user in results.mappings().all()]

    @staticmethod
    def find_one(db: Session, id: int) -> User | None:
        results = db.execute(text(f"SELECT * FROM users WHERE user_id={id}"))

        user = results.mappings().first()

        return User(**user) if user else None

    @staticmethod
    def find_one_by_name(db: Session, name: str) -> User | None:
        results = db.execute(text(f"SELECT * FROM users WHERE name='{name}'"))

        user = results.mappings().first()

        return User(**user) if user else None

    @staticmethod
    def update_one(db: Session, id: int, user: CreateUser) -> User | None:
        db.execute(
            text(
                f"""UPDATE users SET name="{user.name}",
                password="{user.password}" WHERE user_id={id}"""
            )
        )
        db.commit()

        return User(user_id=id, **user.model_dump())

    @staticmethod
    def delete_one(db: Session, id: int) -> int | None:
        results = db.execute(
            text(f"DELETE FROM users WHERE user_id={id} RETURNING user_id")
        )
        db.commit()

        deleted_id = results.first()

        return deleted_id[0] if deleted_id else None
