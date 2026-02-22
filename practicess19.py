# # 
import pandas as pd 
df = pd.read_csv('Mobile_sales_data.csv')
# print(df.dtypes)

#Data Cleaning 
# print(df.isnull().sum())
# print(df.duplicated().sum())
#aur bhi hai but mere table me iska koi kaam na dikh rha hai 

# print(df.head())
# print(df['Brand'].unique())
# print(df['Customer Age']>21)
# print(df['Customer Age'])

print(df.loc[0:2],['Customer Name'])
