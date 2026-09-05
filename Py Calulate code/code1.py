import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#1. Represent Data using pandas

data=pd.DataFrame({
    'Size':[1,2],
    'Price':[3,5]
})

#3 .Generate pounts for the prediction line based on our math (y=2x*1)

x_line=np.linspace(0,3,100)
y_line =2 *x_line+1


#3 .Visualize using Matplotlib

plt.figure(figsize=(8,5))
plt.scatter(data['Size'],data['Price'],color='red',s=100 ,label='Actual Data')
plt.plot(x_line,y_line,color='blue',linewidth=2, label='AI Model: y= 2x+1')

#Formatting
plt.title('House Price Prediction (Linear regression)')
plt.xlabel('Size (1000 sq ft)')
plt.ylabel('Price ($100k)')
plt.xlim(0,3)
plt.ylim(0,6)
plt.legend()
plt.grid(True,linestyle='--',alpha=0.7)
plt.show()