from fastapi import APIRouter

router = APIRouter(prefix="/ingestion", tags=["ingestion"])

@router.post("/")
async def ingest_logs():
    return {"status": "Log ingestion placeholder"}