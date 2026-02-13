from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine

DATABASE_URL = 'postgresql+psycopg://datapulse_user:datapulse_pass@localhost:5432/datapulse'
_engine = None

def get_engine(echo: bool = False) -> Engine:
    global _engine
    if _engine is None:
        try:
            _engine = create_engine(DATABASE_URL, echo = False)
            
            conn = _engine.connect()
            conn.close()
        except Exception as e:
            print(e)
    return _engine

engine = get_engine()
SessionLocal = sessionmaker(bind = engine, autoflush = False, autocommit = False)

Base = declarative_base()