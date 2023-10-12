import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB = os.environ.get("POSTGRES_DB")
DB_NAME = os.environ.get("DB_NAME")
AIO_DB = os.environ.get("AIO_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")



