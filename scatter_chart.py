import matplotlib.pyplot as plt
# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
marks = [45, 50, 55, 60, 65, 70, 75, 78, 82, 85, 88, 90]
#plot
plt.figure(figsize=(10,6))
plt.scatter(study_hours,marks,s=150,cmap='viridis',alpha= 0.8)

#label
plt.title('Study vs marks',fontsize =12,fontweight='bold')
plt.xlabel('Study Hour per week',fontsize =12)
plt.ylabel('Marks',fontsize =12)
plt.grid(True,alpha = 0.3)
plt.show()