import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Data
data = {
'Sales': [10000, 15000, 20000, 25000, 30000, 35000],
'Profit': [2000, 3000, 4000, 5000, 6000, 7000],
'Region': ['North', 'South', 'East', 'West', 'North', 'South']
}
df = pd.DataFrame(data)
# Scatter plot with hue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Profit', hue='Region', data=df, s=100)
plt.title('Sales vs Profit by Region', fontsize=14, fontweight='bold')
plt.xlabel('Sales ( )', fontsize=12)
plt.ylabel('Profit ( )', fontsize=12)
plt.show()