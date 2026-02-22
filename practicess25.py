import pandas as pd
import numpy as np

# Creating the Employee dataset
data = {
    'EmpID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Full_Name': ['Rahul Sharma', 'Sneha Gupta', 'Vikram Singh', 'Pooja Verma', 'Amit Patel', 'Neha Gill', 'Rohan Das', 'Kavita Roy'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [60000, 45000, 72000, 50000, 68000, 52000, 48000, 75000],
    'Joining_Date': ['2020-01-15', '2019-05-20', '2021-03-10', '2018-11-05', '2022-07-25', '2020-09-12', '2019-02-28', '2023-01-10'],
    'Performance_Rating': [4.5, 3.8, 4.2, 3.5, 4.0, 3.9, 4.1, 4.7]
}

df = pd.DataFrame(data)
#Q1: Full_Name column mein first aur last name saath mein hain. 
# Inhe alag karke do naye columns banao: First_Name aur Last_Name
df[['First_Name', 'Last_Name']] = df['Full_Name'].str.split(' ', n=1, expand=True)


# Q2: Custom Logic with Lambda (Apply Function)
df['Bonus'] = df.apply(lambda x: x['Salary'] * 0.10
                        if x['Performance_Rating'] > 4.0 
                        else x['Salary'] * 0.05, axis=1)


#Q3: . Date Manipulation(Join_year)
df['Joining_Date']= pd.to_datetime(df['Joining_Date'])
df['Join_year'] = df['Joining_Date'].dt.year
df['Join_Month'] = df['Joining_Date'].dt.month_name()
df['Join_day'] = df['Joining_Date'].dt.day_name()
# print(df)

#Q4: Complex Filtering
# Wo employees filter karke dikhao jo 'IT' department ke hain AUR jinki Salary 65,000 se zyada hai.
# print(df[(df['Department'] == 'IT') & (df['Salary']> 65000)])


# Q5: Sorting Data(Descending Order (sabse zyada salary pehle))
a = df.sort_values('Salary',ascending= False)
print(a.head(3))


