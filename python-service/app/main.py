from app.services.coin_service import addCoin, getAllCoins, getCoin, addCoinList, removeOldCoins
from app.integrations.coingecko_client import pingConnection, getApiCoins
from app.mappers.coin_mapper import mapListToCoins
'''
async def main():
    # coinsList = await getApiCoins()
    # coinList =  mapListToCoins(coinsList)
    # addCoinList(coinList)
    print(getAllCoins())

asyncio.run(main())
# if __name__ == "__main__":
#     main()
'''

from app.cache.redis_client import get_redis_client

def main():
    redis_client = get_redis_client()
    redis_client.set("ping", "pong")
    value = redis_client.get("ping")
    print(value)

if __name__ == "__main__":
    main()