import numpy as np
import pandas as pd

# Creating the dataset
data = {
    'OrderID': np.arange(101, 111),
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Keyboard', 'Laptop', 'Monitor'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'Region': ['North', 'South', 'East', 'North', 'West', 'East', 'South', 'West', 'North', 'East'],
    'Sales': [1200, 25, 300, 1150, 45, 320, 30, 50, 1250, 310],
    'Quantity': [1, 5, 2, 1, 10, 2, 4, 8, 1, 3],
    'Profit': [150, 5, 40, 140, 10, 45, 6, 12, 160, 42]
}

df = pd.DataFrame(data)

# Introduce some missing values (NaN) for practice
# df.loc[2, 'Sales'] = np.nan
# df.loc[7, 'Profit'] = np.nan

# # Q1: Handling Missing Data:
Missing_data = df['Sales'].fillna(df['Sales'].mean())
Row_drop = df.dropna(subset=['Profit'], inplace=True)


#Q2: Calculate the total Sales and average Profit for each Region.
# Group by Region and calculate sum of Sales and mean of Profit
# q2_answer = df.groupby('Region').agg({
#     'Sales': 'sum',
#     'Profit': 'mean'
# })

# print(q2_answer)

#Q3: Create a new column called Sales_Tax which 
# is 18% of the Sales column. Use a NumPy operation to calculate 
# this (e.g., df['Sales'] * 0.18).
# df['Sales_tax'] = df['Sales']*18



# Q4: Find all rows where the Product is 'Electronics' 
# AND the Quantity sold is greater than or equal to 2.
# print(df[df['Product']=='Electronics') & (df['Quantity']>=2)])

print(df[(df['Category'] == 'Electronics') & (df['Quantity'] >= 2)])

    
# Create a new column called Performance.
# If Profit is greater than 100, label it as "High".
# Otherwise, label it as "Low".
# df['Performance'] = np.where(df['Profit']>100,'High','Low')
# print(df)