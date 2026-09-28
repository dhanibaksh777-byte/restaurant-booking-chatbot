from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()

database_url = os.getenv("DATABASE_URL")
print(database_url.split("@")[-1])
if not database_url:
    raise RuntimeError("database_url does'nt exists!")

engine = create_engine(database_url)
SessionLocal = sessionmaker(bind=engine)
base = declarative_base()


def get_db():
    db  = SessionLocal()
    try:
        yield db

    finally:
        db.close()