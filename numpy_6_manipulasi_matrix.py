import numpy as np

a = np.array((
             [1,2,3],
             [4,5,6]
             ))
             
print ("matriks a dengan  ukuran :",a.shape)
print (a)

# transpose matirks
print ("transpose matrix dari a")
print (a.transpose())
print (np.transpose(a))
print (a.T)

# flaten array, vector, baris
print ("flaten matrix a:")
print (a.ravel())
print (np.ravel(a))

#  reshape matrix
print ("reshape matrix a:")
print (a.reshape(3,2))

# resize matrix
print ("resize matrix a:")
a.resize(3,2)
print (a)
print ("matriks a dengan  ukuran :",a.shape)
