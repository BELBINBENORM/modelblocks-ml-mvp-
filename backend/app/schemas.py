from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class TrainRequest(BaseModel):
    dataset_path: str = Field(..., example="/data/custom.csv")
    target_column: str = Field(..., example="label")
    model_type: str = Field(..., example="xgboost")
    hyperparams: Dict[str, Any] = Field(default_factory=dict)

class TrainResponse(BaseModel):
    job_id: str

class JobStatusResponse(BaseModel):
    job_id: str
    status: str
    progress: int
    result_path: Optional[str] = None
    error: Optional[str] = None
