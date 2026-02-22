import pandas as pd 
df = pd.read_csv('Mobile_sales_data.csv')
df['Total_sales'] = df['Units Sold']*df['Price Per Unit']
df.rename(columns={'Transaction ID':'ID'},inplace=True)

df.drop('Day',axis = 1 , inplace= True)
# 
df['Age_Group'] = df['Customer Age'].apply(lambda x:'Hero'
                                           if x >25 else 'Zero')
df['City']= (df['City'].replace('Ludhiana','Kashmir'))

print(df.head())