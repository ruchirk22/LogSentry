from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path
from backend.services.ingestion_service import save_and_enqueue

router = APIRouter()

ALLOWED_EXT = {'.log', '.txt', '.json', '.tsv'}
MAX_FILES = 10
MAX_BATCH_SIZE = 100 * 1024 * 1024  # 100MB
MAX_FILE_SIZE = 50 * 1024 * 1024    # 50MB

@router.post("/upload")
async def upload_logs(files: list[UploadFile] = File(...)):
    if len(files) > MAX_FILES:
        raise HTTPException(400, f"Max {MAX_FILES} files allowed.")

    total_size = 0
    file_contents = []

    # 1) Read each file once, check extension & size
    for f in files:
        ext = Path(f.filename).suffix.lower()
        if ext not in ALLOWED_EXT:
            raise HTTPException(400, f"Unsupported file: {f.filename}")
        
        content = await f.read()               # Read entire upload
        size = len(content)                    # Get size in bytes
        if size == 0 or size > MAX_FILE_SIZE:
            raise HTTPException(400, f"Invalid size for: {f.filename}")
        
        total_size += size
        file_contents.append((f.filename, content))

    if total_size > MAX_BATCH_SIZE:
        raise HTTPException(400, "Batch exceeds size limit.")

    # 2) Enqueue each file for parsing
    results = []
    for filename, content in file_contents:
        res = save_and_enqueue(filename, content)
        results.append(res)

    return {"detail": results}