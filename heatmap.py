import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Data
data = {
'Temperature': [25, 28, 30, 32, 35, 38, 40],
'Ice_Cream_Sales': [200, 250, 300, 350, 420, 480, 550],
'Cold_Drink_Sales': [150, 180, 220, 260, 320, 380, 450]
}
df = pd.DataFrame(data)
# Correlation matrix
corr = df.corr()
# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='RdYlGn', center=0, square=True)
plt.title('Correlation Heatmap', fontsize=14, fontweight='bold')
plt.show()