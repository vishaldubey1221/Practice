import matplotlib.pyplot as plt 
Students= ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vishal']
Marks= [85, 92, 78, 88, 95]
plt.figure(figsize = (10,6))
plt.bar(Students,Marks,color = ['blue','green','red','orange','purple'],label = 'Marks')
plt.title('Student Marks Comparison',fontsize = 12,fontweight ='bold')
plt.ylabel('Marks')
plt.grid(axis = 'y',alpha = 0.3)
plt.show()