student = {"name":"Vishal",
           "age":20,
           "city":"Dellhi"}
# print(student["age"]) # accessing Value from the data 
#adding and updating data 
student["marks"] = 88 # add the new value
student["age"]= 23
#remove the city
student.pop("city")
print(student.keys())
print(student.values())