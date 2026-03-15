import pandas as pd
import matplotlib.pyplot as plt
Bike_Category= ['Mountain', 'Road', 'Hybrid', 'Mountain', 'Road', 'Hybrid', 'Mountain']
Sales_USD= [1500, 2200, 1800, 1700, 2400, 1600, 1900]
df = pd.DataFrame({'Category': Bike_Category, 'Sales': Sales_USD})
df_grouped = df.groupby('Category')['Sales'].sum().reset_index()


plt.figure(figsize= (10,6))
plt.bar(df_grouped['Category'], df_grouped['Sales'],color = 'yellow',edgecolor='black')
plt.show()