import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('tips')
plt.figure(figsize= (10,6))
sns.histplot(df['total_bill'],kde=True,color = 'blue',bins = 25)
plt.show()