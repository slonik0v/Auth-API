from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from miniauth_api.models import Base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

session = SessionLocal()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
