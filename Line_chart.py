import matplotlib.pyplot as plt
# Data
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
profit = [20000, 25000, 30000, 28000, 35000, 42000, 48000, 55000, 60000, 68000]
# Plot banao
plt.figure(figsize=(10, 6))
plt.plot(years, profit, marker='o', color='red',mfc = 'yellow',mec = 'black', linewidth=2)
# Labels aur title
plt.title('Company Profit Trend (2015-2024)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Profit ( )', fontsize=12)
plt.grid(True, alpha=0.3)
# Dikhao
plt.show()
