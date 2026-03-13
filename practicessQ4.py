import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
data = {
        'city':['Mumbai']*30 + ['Banglore']*30 + ['Delhi']*30,
        'sales': (list(np.random.normal(50000,8000,29))+[10000]
                  +list(np.random.normal(48000,7000,28))+[90000,95000]
                  +list(np.random.normal(52000,9000,30)))
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.boxplot(x='city',y='sales',data = df,palette= 'Set2')
plt.title('Daily sales by city',fontsize = 12,fontweight = 'bold')
plt.xlabel('City',fontsize = 12)
plt.ylabel('sales(₹)')
plt.grid(axis='y', alpha=0.3)
plt.show()