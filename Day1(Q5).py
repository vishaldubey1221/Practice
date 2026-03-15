import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('tips')
plt.figure(figsize=(10,6))
sns.boxplot(x='day',y='total_bill',data = df,palette='Set2')
plt.show()