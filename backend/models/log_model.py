from pydantic import BaseModel

class LogEntry(BaseModel):
    timestamp: str
    message: str