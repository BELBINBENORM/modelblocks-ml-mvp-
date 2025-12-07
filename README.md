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
