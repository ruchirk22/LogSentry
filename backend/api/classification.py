from fastapi import APIRouter

router = APIRouter(prefix="/classification", tags=["classification"])

@router.get("/")
async def classify_logs():
    return {"status": "Classification placeholder"}