import os   
import uuid

from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def generate_uuid():
    return str(uuid.uuid4())