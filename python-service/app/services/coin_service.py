from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import SessionLocal
from app.models.coin import Coin

def addCoin(coin: Coin):
    session = SessionLocal()
    
    try:
        session.add(coin)
        session.commit()
        return coin
    except SQLAlchemyError:
        session.rollback()
        print('Não foi possível adicionar a moeda ao banco!')
        raise
    finally:
        session.close()
        
def addCoinList(coinList: list[Coin]):
    session = SessionLocal()
    
    try:
        for coin in coinList:
            try:
                session.merge(coin)
            except SQLAlchemyError as e:
                print(f'Ocorreu um erro: {e}')
                continue
        session.commit()
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro: {e}')
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