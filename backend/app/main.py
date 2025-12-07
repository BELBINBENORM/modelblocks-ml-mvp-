from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI(title="ModelBlocks Backend", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Health ----
@app.get("/health")
def health():
    return {"status": "ok", "service": "ModelBlocks"}

# ---- Data Upload ----
@app.post("/data/upload")
async def upload_data(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "received"}

# ---- Pipeline Definition ----
class Pipeline(BaseModel):
    nodes: Any
    edges: Any

@app.post("/pipeline/validate")
def validate_pipeline(pipeline: Pipeline):
    if not pipeline.nodes:
        return {"valid": False, "error": "No nodes provided"}
    return {"valid": True}

# ---- Pipeline Execution / Training ----
class TrainRequest(BaseModel):
    pipeline: Dict[str, Any]

@app.post("/train/start")
def start_training(req: TrainRequest):
    job_id = "job_12345"
    return {"status": "queued", "job_id": job_id}

@app.get("/train/status/{job_id}")
def training_status(job_id: str):
    return {"job_id": job_id, "status": "running"}

# ---- Model Export ----
@app.get("/model/{job_id}/export")
def export_model(job_id: str):
    return {"job_id": job_id, "export": "ready"}

# ---- Prediction ----
class PredictRequest(BaseModel):
    job_id: str
    data: Any

@app.post("/predict")
def predict(req: PredictRequest):
    return {"job_id": req.job_id, "prediction": [0.42]}
