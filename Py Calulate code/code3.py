import numpy as np
import matplotlib.pyplot as plt



# 1. Define  Weight vector 
w_vec=np.array([3,4])

#2. Calculate Norm using Numpy
w_norm = np.linalg.norm(w_vec)
print(f"Vector Magnitude (Norm):{w_norm}")


#3 . Visualize
plt.figure(figsize=(8,5))

#Plot the  vector as an arrow from origin 
plt.quiver(0,0,w_vec[0],w_vec[1],angles='xy',scale_units='xy',scale=1,color='purple',width=0.01,
label=f'Weght Vector [3,4]')

#plot a circle to visualize the magnitude (Norm)
circle =plt.Circle((0,0),w_norm ,color='purple',
fill=False,linestyle='--',alpha=0.5,label=f'L2 Norm (Length ={w_norm})')
plt.gca().add_patch(circle)

#Formatting
plt.title('Visualizing Model Complexity via vector norm')
plt.xlabel('Parameter W1 ')
plt.ylabel('Parameter W2 ')
plt.xlim(-1,6)
plt.ylim(-1,6)
plt.axhline(0,color='black',linewidth=0.5)

plt.axvline(0,color='black',linewidth=0.5)
plt.legend()
plt.grid(True,alpha=0.3)
plt.gca().set_aspect('equal',adjustable='box')
#Keep circles circular 
plt.show()