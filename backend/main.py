import uvicorn
from fastapi import FastAPI
from backend.utils.db_init import *  # Creates the table
from backend.api.ingestion import router as ingestion_router


app = FastAPI()
app.include_router(ingestion_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)