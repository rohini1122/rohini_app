from fastapi import FastAPI, Request
from pyarrow import dataset
from pydantic import BaseModel
from typing import List

class DatasetModel(BaseModel):
    dataset_name: str
    dataset_source_id: int #// this is the reference id/key of datasource onboarded (Abhinandan)
    num_of_cols: int
    num_of_rows: int
    is_partitioned: bool
    parition_keys: List[str]
    primary_keys: List[str]
    default_filters: dict