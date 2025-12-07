import time
import traceback
from app.services.job_manager import JobManager

def run_training_job(job_id: str, job_manager: JobManager):
    try:
        job_manager.update_job(job_id, status="running")

        # Fake training loop
        for p in range(0, 101, 20):
            time.sleep(1)
            job_manager.update_job(job_id, progress=p)

        output_path = f"/models/{job_id}/model.bin"

        job_manager.update_job(
            job_id,
            status="completed",
            progress=100,
            result_path=output_path
        )

    except Exception as e:
        job_manager.update_job(
            job_id,
            status="failed",
            error=str(e),
            progress=0
        )
