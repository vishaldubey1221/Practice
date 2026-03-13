import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
#data 
hight = np.random.normal(165,10,100)
plt.figure(figsize = (10,6))
sns.histplot(hight,kde=True,color = 'green',bins = 20)
plt.title('Height Distribution',fontsize = 12,fontweight = 'bold')
plt.xlabel('Height',fontsize = 12)
plt.ylabel('Frequency',fontsize = 12)
plt.show()