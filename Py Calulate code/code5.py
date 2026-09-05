import numpy as np 
import matplotlib.pyplot as plt

#1 .Define Data Matrix
A=np.array([[2,1],
[1,2]])

#2 compute Eigenvalues and Eigenvectors automatically using Numpy

eigenvalues ,eigenvectors =np.linalg.eig(A)
print(f"Eigenvalues (Importance): \n {eigenvalues}")
print(f"Eigenvectors (Principal Direction):\n {eigenvectors}")

#3. Visualize using Matplotlib Quiver (Arrows)
plt.figure(figsize=(8,8))

#define arrows showing directions of spread


#The columns of eigenvectors are the vectors 
v1 =eigenvectors[:,0]*eigenvalues[0] #Scale by eigenvalue for visual import
v2  =eigenvectors[:,1]*eigenvalues[1]

#Plot Eigenvector 1 (primary Axis)
plt.quiver(0,0,v1[0],v1[1],angles='xy',scale_units='xy',scale=1, color='red',width=0.015, label=f'Eigenvector 2 (y={eigenvalues[1]:.1f})')

#Plot Eigenvector 2 (Secondary Axis)
plt.quiver(0,0,v2[0],v2[1],angles='xy',scale_units='xy', scale=1,color='blue',width=0.01,
label=f'Eigenvector 2 (y={eigenvalues[1]:.1f})')

#Formatting 
plt.title('Principal Axis Detection via Eogn Decomposition')
plt.xlabel('Original Feature X')
plt.ylabel('Original Feature y')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.axhline(0,color='black' ,linewidth =1)
plt.axvline(0,color='black',linewidth=1)
plt.gca().set_aspect('equal',adjustable='box') 
#keep aspect ratio squre

plt.legend()
plt.grid(True,alpha=0.3)
plt.show()