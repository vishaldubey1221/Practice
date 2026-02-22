import pandas as pd

# Creating Pizza Sales dataset
data = {
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Pizza_Type': ['Margherita', 'Pepperoni', 'Margherita', 'BBQ Chicken', 'Pepperoni', 'Margherita', 'BBQ Chicken', 'Pepperoni'],
    'Size': ['Regular', 'Large', 'Large', 'Regular', 'Large', 'Regular', 'Large', 'Regular'],
    'Quantity': [2, 1, 3, 1, 2, 1, 2, 1],
    'Price': [199, 399, 299, 249, 399, 199, 449, 249],
    'Order_Date': ['2026-02-18', '2026-02-18', '2026-02-19', '2026-02-19', '2026-02-19', '2026-02-20', '2026-02-20', '2026-02-20']
}

df = pd.DataFrame(data)

# Total Revenue column calculate karke add kar diya hai
df['Revenue'] = df['Quantity'] * df['Price']


# Q1: Har Pizza_Type se total kitni Revenue aayi hai, ye calculate karo.
Total_revenue = df.groupby('Pizza_Type')['Revenue'].sum()
# print(Total_revenue)


#Q2: Ek Pivot Table banao jisme:

# Index (Rows): Pizza_Type ho
# Columns: Size ho
# Values: Quantity ho
# Aggfunc: sum (taaki pata chale kis type ka kaunsa size total kitna bika).
# (Hint: pd.pivot_table(df, ...) ya df.pivot_table(...) use karo).

# pizza_pivot = df.pivot_table(index='Pizza_Type', 
#                              columns='Size', 
#                              values='Quantity',
#                                aggfunc='sum')
# print(pizza_pivot)

# Sirf '2026-02-19' ki date filter karo aur batao ki 
# uss din total kitne Pizzas (Quantity) bike?

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
daily_total = df.groupby('Order_Date')['Revenue'].sum()
print(daily_total)

# filtered_qty = df[df['Order_Date'] == '2026-02-19']['Quantity'].sum()

# print("19th Feb ko total bike hue pizzas:", filtered_qty)