import asyncio
from app.services.coin_service import addCoin, getAllCoins, getCoin, addCoinList
from app.integrations.coingecko_client import pingConnection, getApiCoins
from app.mappers.coin_mapper import mapListToCoins

async def main():
    print(getAllCoins())
#     coinsList = await getApiCoins()
#     coinList =  mapListToCoins(coinsList)
#     print(type(coinList[0]))
#     print(coinList)

asyncio.run(main())
# if __name__ == "__main__":
#     main()
