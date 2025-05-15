from fastapi import APIRouter

router = APIRouter(prefix="/qna", tags=["qna"])

@router.get("/")
async def query_logs():
    return {"status": "Q&A placeholder"}