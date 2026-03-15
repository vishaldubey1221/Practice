import pandas as pd
import matplotlib.pyplot as plt
months=['Jan', 'Feb', 'Mar', 'Apr', 'May']
revenue=[200, 350, 300, 500, 450]

plt.figure(figsize=(10,6))
plt.plot(months,revenue,marker = 'o',color = 'blue',
         label = 'Months',linewidth = 2)
plt.title("Monthly Revenue",fontsize = 12,fontweight = 'bold')
plt.xlabel("Month",fontsize = 12,fontweight = 'bold')
plt.ylabel("Revenue in USD($)",fontsize = 12,fontweight = 'bold')
plt.legend()
plt.grid(True,linestyle='--',alpha = 0.6)
plt.show()