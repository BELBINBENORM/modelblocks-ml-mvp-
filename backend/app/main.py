from fastapi import FastAPI
from app.routers import training

app = FastAPI(
    title="ModelBlocks API",
    version="0.1.0"
)

# Routers
app.include_router(training.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status": "ok", "service": "ModelBlocks API"}
