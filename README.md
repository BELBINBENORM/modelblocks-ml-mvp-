# ModelBlocks-ML (MVP)


Minimal open-source MVP for a visual, node-based ML pipeline runner.


Run locally with Docker (recommended). This MVP provides:
- FastAPI backend with endpoints for upload, pipeline run, model download, predict (basic)
- Trainer skeleton with Keras and PyTorch plugin support
- Simple data connectors (upload, kaggle & s3 stubs)
- Dockerfile and docker-compose for quick deployment


## Quick start (local)


1. Build and run with docker-compose:


```bash
docker compose up --build
```
2. Backend API available at http://localhost:8000

- POST /upload - upload a CSV file
- POST /pipeline/run - submit pipeline JSON (see examples/sample_pipeline.json)
- GET /status/{job_id} - check job status
- GET /model/download/{job_id} - download model artifact (zip)
- POST /predict/{job_id} - quick predict using JSON payload

### Notes

- This is an MVP skeleton. You will want to improve/secure connectors, add queueing (Redis/celery), and harden execution before production.
- For GPU support, build a GPU-capable image and run with nvidia runtime on host.
