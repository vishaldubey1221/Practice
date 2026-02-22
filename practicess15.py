#task 1 : 
# def calucalte_area(l,b):
#     area_ractangle = (l*b)
#     return area_ractangle
# result = calucalte_area(10,20)
# print(result)

#task 2 : to use math libarary find the sqrt of 25 .
# import math
# sqrts = print(math.sqrt(25))


#task 3:
# def is_even(number):
#     if number%2 == 0:
#         return True
#     else:
#         return False
# check  = is_even(211)
# print(check)

#task 4: to use 
#  
import pandas as pd 
data = {
    "Name":["Vishal","Priya","Amit"],
    "age":[20,22,25],
    "Marks":[85,95,65]
}
df = pd.DataFrame(data)
print(df)
Highest_value = df.sort_values(by = "Marks",ascending=False)
print(Highest_value)

# Task 5:
# grade = ["a","b","c","d","e"]
# marks = [85,72,95,60,45]
# def grade_calculator_pro(marks_list, grade_list):
#     marks_list.sort(reverse=True)
#     for m, g in zip(marks_list, grade_list):
#         print(f"Marks: {m} || Grade: {g}")
# grade_calculator_pro(marks,grade)
