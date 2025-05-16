import sqlite3
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "database" / "sqlite" / "logsentry.db"

conn = sqlite3.connect('database/sqlite/logsentry.db')
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    ip TEXT,
    method TEXT,
    url TEXT,
    status INTEGER,
    raw_log TEXT,
    file_name TEXT,
    upload_time TEXT
)
""")
conn.commit()
conn.close()