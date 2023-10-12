
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST
from .models import Base

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_db_and_tables():
    conn = engine.connect()
    Base.metadata.create_all(bind=engine)
    conn.close()


create_db_and_tables()


def get_db():
    db = SessionLocal()
    return db
