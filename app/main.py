from fastapi import FastAPI

app = FastAPI(title="API Test Scaffold")

@app.get("/health")
async def health():
    return {"status": "ok"}
