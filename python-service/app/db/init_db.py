from app.db.database import get_engine, Base
from app.models.coin import Coin

engine = get_engine()

def main():
    Base.metadata.create_all(bind = engine)

if __name__ == '__main__':
    main()