from fastapi import FastAPI

app = FastAPI(title="LogSentry API")

@app.get("/")
async def root():
    return {"message": "Welcome to LogSentry API"}