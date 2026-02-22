# Department-wise average salary nikalo. Konse department mein sabse zyada
# average salary hai?
import pandas as pd 
Data = {'Name':['Amit','Vishal','Shreya','Abhishek','Aariz'],
        'Department':['IT','SALES','IT','HR','HR'],
        'Salary':[45000,50000,52000,48000,56000]}
df = pd.DataFrame(Data)
a = df.groupby('Department')['Salary'].mean()
max_dept = a.idxmax()
max_value = a.max()
print(max_dept,max_value)



# DataFrame mein kuch missing values (NaN) add karo aur phir unhe handle karo - ek
# case mein mean se fill karo, dusre mein rows delete karo.
import pandas as pd 
data = { 'Name': ['Raj', 'Priya', 'Amit', None, 'Vikram'], 'Age': [21,
None, 20, 23, 21], 'Marks': [85, 92, None, 88, None] }
df = pd.DataFrame(data)
# print(df.isnull().sum())
# print(df['Marks'].fillna(df['Marks'].mean(),inplace= True))
print(df.dropna())
