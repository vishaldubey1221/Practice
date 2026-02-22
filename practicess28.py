import pandas as pd
import numpy as np

# Creating the University Exam dataset
data = {
    'Student_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Name': ['Aarav', 'Priya', 'Vikram', 'Neha', 'Rohan', 'Sneha', 'Kabir', 'Pooja'],
    'Subject': ['Statistics', 'Computer Science', 'Maths', 'Statistics', 'Computer Science', 'Maths', 'Statistics', 'Computer Science'],
    'Score': [85, 92, 78, np.nan, 88, 95, 65, np.nan],
    'Attendance_Percentage': [90, 85, 75, 80, 95, 82, 60, 88]
}

df = pd.DataFrame(data)

# Q1: Handling Missing Data
df['Score'] = df['Score'].fillna(df['Score'].mean())
# print(df)


#Q2: Complex Logic (NumPy where)

df['Result'] = np.where((df['Score']>=40) & (df['Attendance_Percentage']>=75),'Pass','Fail')
# print(df)

#Q3:Grouping and Aggregation
u = df.groupby('Subject')['Score'].agg(['max','min'])
# print(u)


#Q4:String Manipulation
# print(df['Name'].str.upper())


#Q5: Filtering and Sorting
# Pehle filter karo
passed_students = df[df['Result'] == 'Pass']

# Phir us filtered data ko sort karo
final_result = passed_students.sort_values('Score', ascending=False)

print(final_result)


