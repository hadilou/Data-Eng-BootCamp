#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
from sqlalchemy import create_engine

df = pd.read_parquet("yellow_tripdata_2022-01.parquet"

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
                     
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')




