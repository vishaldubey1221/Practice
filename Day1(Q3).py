import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
data = np.random.normal(80,20,100)
plt.figure(figsize=(10,6))
sns.histplot(data,kde=True,color='red',bins =25)
plt.title("DATA",fontsize = 12,fontweight = 'bold')
plt.xlabel("data",fontsize = 12,fontweight = 'bold')
plt.ylabel("frequency",fontsize = 12,fontweight = 'bold')
plt.show()