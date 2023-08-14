from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO env
# TODO test db
SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://gauer:qweasdzxc@127.0.0.1:3306/stock"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
