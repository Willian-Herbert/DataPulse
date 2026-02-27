from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import SessionLocal
from app.models.coin import Coin
from app.core.logger import get_logger
from app.cache.redis_client import getRedisClient
from redis.exceptions import RedisError
import json

CACHE_KEY = 'coins:top100'
CACHE_TTL = 60
logger = get_logger(__name__)

def addCoin(coin: Coin):
    session = SessionLocal()
    
    try:
        session.add(coin)
        session.commit()
        return coin
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f'Não foi possível adicionar a moeda ao banco: {e}', exc_info=True)
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
                logger.error(f'Ocorreu um erro: {e}', exc_info=True)
                continue
        session.commit()
        invalidateTopCoinsCache()
    except Exception as e:
        session.rollback()
        logger.error(f'Ocorreu um erro: {e}', exc_info=True)
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
        logger.error(f'Não foi possível buscar os dados: {e}', exc_info=True)
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
        logger.error(f'Não foi possível buscar a moeda escolhida: {e}', exc_info=True)
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
        logger.info('Limpando moedas antigas')
        try:
            for oldCoin in baseList:
                coin = session.execute(select(Coin).filter_by(id = oldCoin)).scalar()
                session.delete(coin)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            logger.error(f'Falha ao remover moedas: {e}', exc_info=True)
    else:
        logger.info('Sem moedas novas')
        
def getTopCoinsCached():
    try:
        redisClient = getRedisClient()
        
        cached = redisClient.get(CACHE_KEY)
        if cached:
            logger.info('Hit Redis')
            return json.loads(cached)
    except RedisError as e:
        logger.warning(f'Redis indisponível: {e}')
        
    logger.info('Miss Redis')    
    coins = getAllCoins()
    serialized = [
        {
            'id': c.id,
            'name': c.name,
            'symbol': c.symbol,
            'market_rank': int(c.market_rank),
            'price': float(c.price),
            'market_cap': float(c.market_cap),
            'image': c.image
        }
        for c in coins
    ]
    
    try:    
        redisClient.set(
            CACHE_KEY,
            json.dumps(serialized),
            ex=CACHE_TTL
        )
    except RedisError as e:
        logger.warning(f'Redis indisponível: {e}')
        
    return serialized
    

def invalidateTopCoinsCache():
    redisClient = getRedisClient()
    redisClient.delete(CACHE_KEY)