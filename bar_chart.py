import matplotlib.pyplot as plt
categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Toys']
sales = [45000, 38000, 52000, 28000, 35000]
# Plot
plt.figure(figsize=(10, 6))
plt.bar(categories, sales, color=['blue', 'green', 'orange', 'red', 'purple'])
plt.plot(categories, sales, color='black', marker='o', linestyle='-', linewidth=2, markersize=8)
# Labels
plt.title('Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Sales ( )', fontsize=12)
plt.xticks(rotation=0)  # Category names ko 45 degree pe ghuma do
plt.grid(axis='y', alpha=0.3)
plt.show()