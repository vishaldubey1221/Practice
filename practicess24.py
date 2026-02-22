# import pandas as pd 
# data = { 'City': ['Delhi',
# 'Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi'], 'Category': ['Electronics',
# 'Clothing', 'Electronics', 'Electronics', 'Clothing', 'Clothing'], 'Sales':
# [50000, 30000, 80000, 45000, 35000, 25000] } 
# df = pd.DataFrame(data)
# # a = df.groupby('City')['Sales'].sum()
# # print(a)
# # b = df.groupby('Category')['Sales'].sum()
# # print(b)
# summary = df.groupby(['City','Category'])['Sales'].agg(['sum', 'mean', 'count'])
# print(summary)





#  Ek complete mini-project: Students DataFrame mein Grade column add karo (A, B,
# C based on marks), phir Grade-wise count nikalo aur result ko bar chart mein visualize
# karne ke liye data ready karo.
import pandas as pd 
import numpy as np


0