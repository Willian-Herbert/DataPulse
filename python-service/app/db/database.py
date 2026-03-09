from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine
from app.core.logger import get_logger
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DATABASE_URL = f'postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

_engine = None
logger = get_logger(__name__)

def get_engine(echo: bool = False) -> Engine:
    global _engine
    if _engine is None:
        try:
            _engine = create_engine(DATABASE_URL, echo = False)
            
            conn = _engine.connect()
            conn.close()
        except Exception as e:
            logger.error(e)
    return _engine

engine = get_engine()
SessionLocal = sessionmaker(bind = engine, autoflush = False, autocommit = False)

Base = declarative_base()