
import matplotlib.pyplot as plt
Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
Temperature = [15, 18, 22, 28, 32, 35]


plt.figure(figsize= (10,6))
plt.plot(Months,Temperature,marker = 'o',color='green',mfc = 'yellow',mec = 'black', linewidth=2,label='Temperature')
plt.title('Monthly Temperature')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()