import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Data (100 students ke grades)
data = {
'Grade': ['A']*30 + ['B']*45 + ['C']*25
}
df = pd.DataFrame(data)
# Count Plot (automatically count karega)
plt.figure(figsize=(8, 6))
sns.countplot(x ='Grade', data=df, palette='viridis')
plt.title('Grade Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Grade', fontsize=12)
plt.ylabel('Number of Students', fontsize=12)
plt.show()