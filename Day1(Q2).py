import matplotlib.pyplot as plt
sections = ['Section A', 'Section B', 'Section C']
scores = [85, 78, 92]

plt.figure(figsize=(10,6))
plt.bar(sections,scores,color = 'green')
plt.title("Section wise score",fontsize = 12,fontweight = 'bold')
plt.xlabel("section",fontsize = 12,fontweight = 'bold')
plt.ylabel("score",fontsize = 12,fontweight = 'bold')
plt.grid(axis = 'y',linestyle='--',alpha = 0.6)
plt.show()
