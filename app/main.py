
from fastapi import FastAPI
import pyarrow.parquet as pq
import pyarrow.dataset as ds
import pyarrow as pa
from config.settings import Settings

import os


app = FastAPI()
settings=Settings()


def get_parquet_schema(file_path):
   
   dataset = ds.dataset(file_path, format='parquet')
   schema = dataset.schema.to_arrow_schema()
   schema = schema.append(pa.field('email', pa.string()))

   column_mapping = {
   'int32': 'INT',
   'int64': 'BIGINT',
   'float32': 'FLOAT',
   'float64': 'DOUBLE',
   # Add more mappings as needed

   }

   json_contract = {'field1': 'value1', 'field2': 'value2'} # Replace with your JSON contract
   for field_name, field_value in json_contract.items():
      field_type = type(field_value).__name__
      if field_type in column_mapping:
         field = pa.field(field_name, pa.string() if field_type == 'str' else column_mapping[field_type])
   else:
      field = pa.field(field_name, pa.string())
   schema = schema.append(field)
   return schema