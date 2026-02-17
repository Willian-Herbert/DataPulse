import asyncio
from app.services.coin_service import addCoin, getAllCoins, getCoin, addCoinList, removeOldCoins
from app.integrations.coingecko_client import pingConnection, getApiCoins
from app.mappers.coin_mapper import mapListToCoins

async def main():
    coinsList = await getApiCoins()
    coinList =  mapListToCoins(coinsList)
    removeOldCoins(coinList)
    # print(getAllCoins())

asyncio.run(main())
# if __name__ == "__main__":
#     main()
