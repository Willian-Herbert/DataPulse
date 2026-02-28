from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine
from app.core.logger import get_logger

DATABASE_URL = 'postgresql+psycopg://datapulse_user:datapulse_pass@localhost:5432/datapulse'
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