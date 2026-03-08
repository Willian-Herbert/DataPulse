from fastapi import APIRouter
from app.core.logger import get_logger
from app.services.coin_service import getTopCoinsCached

logger = get_logger(__name__)

router = APIRouter(
    prefix="/coins",
    tags=["Coins"]
)

@router.get("/health")
def healthCheck():
    return {"status": "ok"}

@router.get("/top")
async def getTopCoins():
    logger.info("Request recebida: GET /coins/top")

    coins = await getTopCoinsCached()

    return {
        "count": len(coins),
        "data": coins
    }