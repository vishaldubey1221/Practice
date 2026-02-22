import pandas as pd 
data = {'City': ['Delhi', 'Mumbai',
'Delhi', 'Mumbai', 'Bangalore'], 'Product': ['TV', 'Mobile', 'Laptop', 'TV',
'Mobile'], 'Sales': [50000, 30000, 80000, 45000, 35000]} 
df = pd.DataFrame(data)
# city_sales = df.groupby('City')['Sales'].sum()
# summary = df.groupby('City')['Sales'].agg(['sum','mean'])
# summary = df.groupby('City')['Sales'].aggregate(['sum','mean'])
# print(summary)
# product_City  = df.groupby(['City','Product'])['Sales'].sum()
# print(product_City)
print(df['Product'].value_counts())