import aiohttp
import asyncio
from app.core.logger import get_logger

API_KEY = 'CG-2NVYRDi8YzhtW9Syov4Y82YY'
logger = get_logger(__name__)

async def pingConnection():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://api.coingecko.com/api/v3/ping?x_cg_demo_api_key={API_KEY}') as response:
            logger.info(await response.text())
            
async def getApiCoins():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=brl&include_tokens=top&x_cg_demo_api_key={API_KEY}') as response:
                return await response.json()
    except Exception as e:
        logger.error(f'Não foi possível buscar os dados: {e}', exc_info=True)
        return []
