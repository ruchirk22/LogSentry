from fastapi import APIRouter

router = APIRouter(prefix="/clustering", tags=["clustering"])

@router.get("/")
async def cluster_logs():
    return {"status": "Clustering placeholder"}