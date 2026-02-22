students = { "Amit": 78, "Deepak": 85, "Ravi": 35, "Neha": 92, "Kiran": 60 }
print("Total Marks",sum(students.values()))
import statistics
avg = statistics.mean(students.values())
print("Avg of all the marks :",avg)
print("Highest Marks :",max(students.values()))
print("Lowest Marks :",min(students.values()))

for name , marks in students.items():
    if marks>40:
        print(f"{name}:pass")
    else:
        print(f"{name}:Fail")


pass_Count = len([marks for marks in students.values() if marks>40])
print("total people passed :-",pass_Count)







