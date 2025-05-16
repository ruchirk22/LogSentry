# backend/services/celery_app.py
from celery import Celery
from backend.config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

celery_app = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)
celery_app.conf.task_routes = {'services.ingestion_service.parse_and_store': {'queue': 'ingest'}}
celery_app.autodiscover_tasks(['backend.services.ingestion_service'])
