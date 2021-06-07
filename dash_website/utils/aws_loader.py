from boto3 import client
from botocore.client import Config

import os
from io import BytesIO
import numpy as np
import pandas as pd


AWS_BUCKET_NAME = "age-prediction-site"
CLIENT = client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    config=Config(signature_version="s3v4"),
)


def load_npy(key_in_bucket):
    obj = CLIENT.get_object(Bucket=AWS_BUCKET_NAME, Key=key_in_bucket)
    return np.load(BytesIO(obj["Body"].read()))


def load_feather(key_in_bucket, **kwargs):
    obj = CLIENT.get_object(Bucket=AWS_BUCKET_NAME, Key=key_in_bucket)
    return pd.read_feather(BytesIO(obj["Body"].read()), **kwargs)
