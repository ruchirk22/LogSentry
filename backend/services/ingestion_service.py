import os
import uuid
import datetime
from pathlib import Path

from huggingface_hub import upload_file
from backend.services.celery_app import celery_app
from backend.services.db_service import store_logs
from backend.utils.log_parser import detect_and_parse

UPLOAD_DIR = Path('uploads')
UPLOAD_DIR.mkdir(exist_ok=True)

def save_and_enqueue(filename: str, content: bytes):
    file_id = uuid.uuid4().hex
    path = UPLOAD_DIR / f"{file_id}_{filename}"
    with open(path, 'wb') as f:
        f.write(content)
    task = parse_and_store.delay(str(path))
    return {"file": filename, "task_id": task.id}

@celery_app.task(name='backend.services.ingestion_service.parse_and_store')
def parse_and_store(path):
    print(f"[parse_and_store] Processing {path}")
    records = detect_and_parse(path)
    print(f"[parse_and_store] Parsed {len(records)} records")
    store_logs(records, path, upload_file)
    print(f"[parse_and_store] Stored records, cleaning up {path}")
    os.remove(path)
    return {"parsed": len(records)}
