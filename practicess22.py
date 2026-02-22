# Q1. print the even number from (2 to 100)
# import numpy as np 
# even_number = np.arange(2,101,2)
# print(even_number)

# Q2: find the mean , median, std ?
# import numpy as np 
# a = np.array([23,45,67,12,89,34,56])
# Mean_value = np.mean(a)
# print(f"Mean is the :{Mean_value}")
# Median_value = np.median(a)
# print(f"Median is the :{Median_value}")
# Std_value = np.std(a)
# print(f"Std is the :{Std_value}")

#Q3: Pandas DataFrame banao jisme 5 employees
#  ka Name, Department, aur Salary ho.
# Phir sirf un employees ko filter karo
# jinki salary 50000 se zyada hai.

import pandas as pd 
Data = {'Name':['Amit','Vishal','Shreya','Abhishek','Aariz'],
        'Department':['IT','SALES','IT','HR','HR'],
        'Salary':[45000,50000,52000,48000,56000]}
df = pd.DataFrame(Data)
# high_salary = (df[df['Salary']>50000])
# print(high_salary)


#Q4: Upar wale DataFrame mein ek naya column 'Tax'
#  add karo jo salary ka 10% ho. Phir
# 'Net Salary' column add karo (Salary - Tax).
df['Net_salary'] = (df['Salary']*0.1)+(df['Salary'])
print(df.head())