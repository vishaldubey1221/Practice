import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('tips')
sns.scatterplot(data=df, x='total_bill', y='tip', hue='time', style='time', s=100)


plt.title("Relationship between Total Bill and Tip", fontsize=14, fontweight='bold')
plt.xlabel("Total Bill ($)", fontsize=12)
plt.ylabel("Tip ($)", fontsize=12)


plt.show()