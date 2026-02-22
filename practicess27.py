import pandas as pd

# Table 1: Customers Data
customers = pd.DataFrame({
    'CustomerID': [101, 102, 103, 104, 105],
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Vikram'],
    'City': ['DEL', 'BOM', 'BLR', 'DEL', 'PUN']
})

# Table 2: Orders Data
orders = pd.DataFrame({
    'OrderID': [1, 2, 3, 4, 5, 6],
    'CustomerID': [101, 102, 101, 104, 105, 101], 
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer', 'Keyboard'],
    'Amount': [55000, 1500, 2500, 12000, 8000, 2500], # Order 3 aur 6 bilkul same hain
    'Order_Date': ['2026-02-15', '2026-02-16', '2026-02-17', '2026-02-18', '2026-02-19', '2026-02-17']
})

# print("Customers Table:\n", customers, "\n")
# print("Orders Table:\n", orders)



# Q1: Merging DataFrames (Inner Join)
merge_df = pd.merge(customers,orders ,on = 'CustomerID',how= 'inner')
# print(merge_df)

#Q2: Handling Duplicates
merge_df.drop_duplicates(inplace=True)
print(merge_df)

print(merge_df.duplicated().sum())
merge_df.drop_duplicates(inplace= True)
# print(merge_df)



# Q3: Data Replacement (Cleaning)
merge_df['City'] = merge_df['City'].replace({'DEL': 'Delhi', 
                                            'BOM': 'Mumbai', 
                                            'BLR': 'Banglore', 
                                              'PUN': 'Pune'})
print(merge_df)


#Q4: Date Filtering (Between Dates)
merge_df['Order_Date'] = pd.to_datetime(merge_df['Order_Date'])
#  Bhai 4 wala question smjh nhi aa rha tha kya krta mai :


# Q5: Grouping on Merged Data
City_sales = merge_df.groupby('City')['Amount'].sum()
print(f'City_sales {City_sales}')






filtered_dates = merge_df[merge_df['Order_Date'].between('2026-02-16', '2026-02-18')]

print("Filtered Data:\n", filtered_dates)