from app.services.coin_service import addCoin, getAllCoins

def main():
    coins = getAllCoins()
    print(coins[0].id)

if __name__ == "__main__":
    main()
