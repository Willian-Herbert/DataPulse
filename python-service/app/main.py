import asyncio
from app.services.coin_service import addCoin, getAllCoins, getCoin
from app.integrations.coingecko_client import pingConnection, getApiCoins

def main():
    asyncio.run(getApiCoins())

if __name__ == "__main__":
    main()
