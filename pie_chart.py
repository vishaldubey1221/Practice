import matplotlib.pyplot as plt

# Fixed spelling for categories
categories = ['Housing', 'Education', 'Food', 'Entertainment', 'Utilities']
expenses = [1200, 600, 300, 200, 150]

# Define the explode parameter as a tuple of numbers, one for each category. 
# 0.1 pulls the first slice ('Housing') out slightly.
# explode_values = (0.1, 0, 0, 0, 0) 

plt.figure(figsize=(8,6))

# Added the 'labels' parameter and fixed 'explode'
plt.pie(expenses, 
        labels=categories, 
        colors=('red', 'blue', 'green', 'yellow', 'orange'),
        autopct='%1.1f%%',
        shadow=True, 
        startangle=140)

plt.title('Monthly Expenses', fontsize=16, pad=20)
plt.axis('equal')
plt.show()