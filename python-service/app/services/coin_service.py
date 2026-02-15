from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import SessionLocal
from app.models.coin import Coin

def addCoin(id: str, name: str, symbol: str, price, market_cap: int):
    session = SessionLocal()
    
    try:
        coin = Coin(
            id = id,
            name = name,
            symbol = symbol,
            price = price,
            market_cap = market_cap
        )
        session.add(coin)
        session.commit()
        return coin
    except SQLAlchemyError:
        session.rollback()
        print('Não foi possível adicionar a moeda ao banco!')
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
    except Exception as e:
        print('Não foi possível buscar os dados!' + e)
        raise
    finally:
        session.close()
        
def getCoin(coinId: str):
    session = SessionLocal()
    
    try:
        stmt = select(Coin).where(Coin.id == coinId)
        data = session.execute(stmt)
        coin = data.scalar()
        return coin
    except Exception as e:
        print('Não foi possível buscar a moeda escolhida!' + e)
        raise
    finally:
        session.close()