import pytest
import os
from dotenv import load_dotenv
import uuid

load_dotenv()


@pytest.fixture()
def bucket():
    return os.environ["PANGEO_TEST_BUCKET"]


@pytest.fixture()
def tmp_gcs_path(bucket):
    return os.path.join(bucket, uuid.uuid4().hex)
