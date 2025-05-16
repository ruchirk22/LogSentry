import sqlite3
from elasticsearch import Elasticsearch
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "sqlite" / "logsentry.db"

es = Elasticsearch()

# backend/services/db_service.py
import logging
logger = logging.getLogger("ingestion")

def store_logs(records, path, upload_time):
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    for r in records:
        try:
            c.execute(
                "INSERT INTO logs(...) VALUES (?,?,?,?,?,?,?,?)",
                (r['timestamp'], r['ip'], r['method'], r['url'],
                 r['status'], r['raw_log'], str(path), upload_time)
            )
        except Exception as e:
            logger.error(f"Failed to insert record from {path}: {e}")
    conn.commit()
    conn.close()
    logger.info(f"Stored {len(records)} records from {path}")
