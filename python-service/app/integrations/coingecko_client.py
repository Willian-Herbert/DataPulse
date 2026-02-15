import aiohttp
import asyncio

API_KEY = 'CG-2NVYRDi8YzhtW9Syov4Y82YY'

async def pingConnection():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.coingecko.com/api/v3/ping?x_cg_demo_api_key={API_KEY}') as response:
            print(await response.text())
            
async def getApiCoins():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&include_tokens=top&x_cg_demo_api_key={API_KEY}') as response:
                return response.text()
    except Exception as e:
        print('Não foi possível buscar os dados!' + e)
        return []
    
