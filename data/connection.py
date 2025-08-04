from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, create_engine
from databases import Database
from dotenv import load_dotenv
from os import getenv

Base = declarative_base()

load_dotenv()

DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = Database(DATABASE_URL)
metadata = MetaData()


async def startup():
    await database.connect()
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


async def shutdown():
    await database.disconnect()
