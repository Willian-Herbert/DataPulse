from app.models.coin import Coin

def mapDictToCoin(dict: dict) -> Coin:
    return Coin(
        id = dict['id'],
        name = dict['name'],
        symbol = dict['symbol'],
        market_rank = dict['market_cap_rank'],
        price = dict['current_price'],
        market_cap = dict['market_cap'],
        image = dict['image']
    )
    
def mapListToCoins(list: list[dict]) -> list[Coin]:
    return [mapDictToCoin(dict) for dict in list]