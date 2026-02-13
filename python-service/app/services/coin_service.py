from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import SessionLocal
from app.models.coin import Coin

def addCoin(id: str, symbol: str, price, market_cap: int):
    session = SessionLocal()
    
    try:
        coin = Coin(
            id = id,
            symbol = symbol,
            price = price,
            market_cap = market_cap
        )
        session.add(coin)
        session.commit()
        return coin
    except SQLAlchemyError:
        session.rollback()
        print('Deu pau')
        raise
    finally:
        session.close()
    
def getAllCoins():
    session = SessionLocal()
    
    try:
        stmt = select(Coin)
        data = session.execute(stmt)
        coins = data.scalars().all()
        return coins
    except:
        print('Não foi possível buscar os dados')
        raise
    finally:
        session.close()