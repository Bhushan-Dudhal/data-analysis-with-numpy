import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt



#1. Create a pandas DaataFrame representing the raw table 
df_raw =pd.DataFrame({
'Size_1000sqft':[1.5,2.1,0.9],
'Price_100k':[3.2,4.5,2.1]
},index=['Property A','Property B','Property C']
)

print("Human-Readable dataFrame :")
print(df_raw)
print("_"*20)


#2. Convert toa pure mathematical NumPy Matrix (Feature Matrix X)

# The indexing and column names are dropped , leaving just numerical data
X_matrix =df_raw.values


print("Mathematical Feature Matrix (X):")
print(X_matrix)
print(f"Shape of Matrix (Samples,Features): {X_matrix.shape}")


# 3. Basic Visualix=zation of Matrix Data
plt.figure(figsize=(8,5))
plt.scatter(df_raw['Size_1000sqft'],
df_raw['Price_100k'],color="blue" ,s=150)

#Annotate points
for i, text in  enumerate(df_raw.index):
    plt.annotate(text,(df_raw['Size_1000sqft'].iloc[i],
df_raw['Price_100k'].iloc[i]),xytext=(5,5),
textcoords='offset points')


#Formatting 
plt.title('Representing Real Estate Data in Feature Space')
plt.xlabel('Feature Column 1 (Size)')
plt.ylabel('Feature Column 2 (Price)')
plt.grid(True,alpha=0.3)

plt.show()