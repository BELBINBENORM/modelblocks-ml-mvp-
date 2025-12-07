from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.schemas import TrainRequest, TrainResponse, JobStatusResponse
from app.services.job_manager import JobManager
from app.services.trainer import run_training_job

router = APIRouter(tags=["training"])
job_manager = JobManager()

@router.post("/train", response_model=TrainResponse)
async def train_model(req: TrainRequest, bg: BackgroundTasks):
    job_id = job_manager.create_job(req.model_dump())

    bg.add_task(run_training_job, job_id, job_manager)

    return TrainResponse(job_id=job_id)

@router.get("/train/{job_id}", response_model=JobStatusResponse)
async def check_status(job_id: str):
    job = job_manager.get_job(job_id)

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return JobStatusResponse(**job)
