from fastapi import APIRouter

router = APIRouter(
    prefix="/coins",
    tags=["Coins"]
)

@router.get("/health")
def health_check():
    return {"status": "ok"}