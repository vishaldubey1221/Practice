import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Math': np.random.normal(75, 20, 20),
    'Physics': np.random.normal(40, 20, 20), 
    'Chemistry': np.random.normal(70, 20, 20),
    'English': np.random.normal(62, 22, 20)
}

df = pd.DataFrame(data)

corr = df.corr()

plt.figure(figsize=(8,6))


sns.heatmap(corr, annot=True, cmap='RdYlGn', center=0, square=True)

plt.title("Vishal Dubey", fontweight='bold', fontsize=12) 

plt.show()