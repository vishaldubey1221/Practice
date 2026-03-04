import matplotlib.pyplot as plt
# 2x2 grid banaenge (2 rows, 2 columns)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
# Plot 1: Line
ax1.plot([1,2,3,4,5], [2,4,6,8,10], 'o-')
ax1.set_title('Line Plot')
ax1.grid(True)
# Plot 2: Bar
ax2.bar(['A', 'B', 'C', 'D'], [15, 25, 20, 30], color='green')
ax2.set_title('Bar Chart')
# Plot 3: Scatter
ax3.scatter([1,2,3,4,5], [5,7,8,6,9], c='red')
ax3.set_title('Scatter Plot')
# Plot 4: (aur koi chart)
ax4.hist([10,20,30,40,50,60,70], bins=4, color='purple')
ax4.set_title('Histogram')
plt.tight_layout()  # Graphs ko properly adjust karta hai
plt.show()