from fastapi import APIRouter

router = APIRouter(prefix="/summarization", tags=["summarization"])

@router.get("/")
async def summarize_logs():
    return {"status": "Summarization placeholder"}