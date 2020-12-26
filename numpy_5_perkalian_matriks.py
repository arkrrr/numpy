import numpy as np

a = np.array(([5,2],
              [3,5]))
              
b = np.ones([2,2])

print ("matrix a :")
print (a)

print ("matrix b :")
print (b)

# perkalian matrix
c1 = np.dot(a,b)
c2 = a.dot(b)

print ("matrix c1 :")
print (c1)

print ("matrix c2 :")
print (c2)