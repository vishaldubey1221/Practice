import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Data_create
data = {
'Region': ['North']*50 + ['South']*50 + ['East']*50 + ['West']*50,
'Sales': list(np.random.normal(50000, 10000, 50)) + 
list(np.random.normal(45000, 12000, 50)) +
list(np.random.normal(48000, 9000, 50)) +
list(np.random.normal(52000, 11000, 50))}
df = pd.DataFrame(data)
# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Sales', data=df, palette='Set2')
plt.title('Sales Distribution by Region', fontsize=14, fontweight='bold')
plt.ylabel('Sales (₹)', fontsize=12)
plt.show()

