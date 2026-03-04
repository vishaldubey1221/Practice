import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data_Create;
marks = np.random.normal(75,10,1000)
# histogram with KDE
plt.figure(figsize=(10,6))
sns.histplot(marks,kde= True,color='red',bins = 30)

plt.title('Marks distribution with KDE',fontsize = 14,fontweight = 'bold')
plt.xlabel('Marks',fontsize = 12)
plt.ylabel('Frequency',fontsize = 12)
plt.show()