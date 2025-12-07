import os
import zipfile
from kaggle import api as kaggle_api
import boto3


# Minimal connector helpers - production needs more error handling & security.


def fetch_from_kaggle(dataset: str, dest_dir: str) -> str:
# dataset example: 'zynicide/wine-reviews'
out = os.path.join(dest_dir, f"kaggle_{dataset.replace('/','_')}.zip")
kaggle_api.dataset_download_files(dataset, path=dest_dir, unzip=True)
return dest_dir




def fetch_from_s3(bucket: str, key: str, aws_region=None, dest_dir: str = "/app/data") -> str:
s3 = boto3.client('s3')
dest = os.path.join(dest_dir, os.path.basename(key))
s3.download_file(bucket, key, dest)
return dest
