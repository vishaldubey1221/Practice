import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wahi same data
data = {
    'Region': ['North']*50 + ['South']*50 + ['East']*50 + ['West']*50,
    'Sales': list(np.random.normal(50000, 10000, 50)) + 
             list(np.random.normal(45000, 12000, 50)) +
             list(np.random.normal(48000, 9000, 50)) +
             list(np.random.normal(52000, 11000, 50))
}
df = pd.DataFrame(data)

# Background ko thoda clean karte hain
sns.set_style("whitegrid")

# Ek saath 4 graphs dikhane ke liye 2x2 ka canvas banaya
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Seaborn Themes Comparison', fontsize=18, fontweight='bold')

# 1. Viridis Theme
sns.boxplot(ax=axes[0, 0], x='Region', y='Sales', data=df, palette='viridis')
axes[0, 0].set_title("Theme 1: 'viridis'")

# 2. Husl Theme
sns.boxplot(ax=axes[0, 1], x='Region', y='Sales', data=df, palette='husl')
axes[0, 1].set_title("Theme 2: 'husl'")

# 3. Pastel Theme
sns.boxplot(ax=axes[1, 0], x='Region', y='Sales', data=df, palette='Pastel1')
axes[1, 0].set_title("Theme 3: 'Pastel1'")

# 4. Magma Theme
sns.boxplot(ax=axes[1, 1], x='Region', y='Sales', data=df, palette='magma')
axes[1, 1].set_title("Theme 4: 'magma'")

plt.tight_layout()
plt.show()