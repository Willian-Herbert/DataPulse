'''
from app.services.coin_service import addCoin, getAllCoins, getCoin, addCoinList, removeOldCoins, getTopCoinsCached
from app.integrations.coingecko_client import pingConnection, getApiCoins
from app.mappers.coin_mapper import mapListToCoins
async def main():
    # coinsList = await getApiCoins()
    # coinList =  mapListToCoins(coinsList)
    # addCoinList(coinList)
    print(getAllCoins())

asyncio.run(main())
# if __name__ == "__main__":
#     main()

def main():
    print(getTopCoinsCached())

if __name__ == "__main__":
    main()
'''

from fastapi import FastAPI
from app.api.routes import coins
from app.core.logger import get_logger

logger = get_logger(__name__)

def create_app() -> FastAPI:
    app = FastAPI(
        title="DataPulse API",
        version="0.1.0"
    )

    app.include_router(coins.router)

    return app

app = create_app()