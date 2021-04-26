import pyarrow as pa
import pyarrow.parquet as pq 
import numpy as np
import pandas as pd
import sys

def get_all_parquet_database(url, path, **kwargs):
    t = pd.read_csv(url)
    t["year"] = t["时间"].str[0:4]
    t["month"] = t["时间"].str[5:7]
    temp_table = pa.Table.from_pandas(t)
    pq.write_to_dataset(
        temp_table, path, partition_cols=["year", "month"],
    )

if __name__ == "__main__":
    current_url = "1.csv"
    save_path = "c:/Users/jinzh/internship2021/test"
    get_all_parquet_database(current_url, save_path)
    
    