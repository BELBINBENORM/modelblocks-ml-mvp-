import os
import json
from typing import Any


BASE_DIR = os.getenv('BASE_DIR', '/app')
DATA_DIR = os.getenv('DATA_DIR', '/app/data')
MODEL_DIR = os.getenv('MODEL_DIR', '/app/models')


os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)


def save_json(path: str, obj: Any):
with open(path, 'w') as f:
json.dump(obj, f, indent=2)


def load_json(path: str):
with open(path) as f:
return json.load(f)
