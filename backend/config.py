import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///logsentry.db")
    ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost:9200")