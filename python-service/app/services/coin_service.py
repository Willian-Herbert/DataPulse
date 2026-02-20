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
    except SQLAlchemyError as e:
        session.rollback()
        print(f'Não foi possível adicionar a moeda ao banco! {e}')
        raise
    finally:
        session.close()
        
def addCoinList(coinList: list[Coin]):
    session = SessionLocal()
    removeOldCoins(coinList, session)
    
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
        stmt = select(Coin).order_by(Coin.market_rank.asc())
        data = session.execute(stmt)
        coins = list(data.scalars().all())
        return coins
    except Exception as e:
        print(f'Não foi possível buscar os dados! {e}')
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
        print(f'Não foi possível buscar a moeda escolhida! {e}')
        raise
    finally:
        session.close()
        
def removeOldCoins(apiList: list[Coin], session):
    data = session.execute(select(Coin.id))
    baseList = list(data.scalars().all())
    
    for newCoin in apiList:    
        try:
            index = baseList.index(newCoin.id)
            baseList.pop(index)
        except:
            continue
    
    if baseList != []:
        print('Limpando moedas antigas')
        try:
            for oldCoin in baseList:
                coin = session.execute(select(Coin).filter_by(id = oldCoin)).scalar()
                session.delete(coin)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f'Falha ao remover moedas! {e}')
    else:
        print('Sem moedas novas')