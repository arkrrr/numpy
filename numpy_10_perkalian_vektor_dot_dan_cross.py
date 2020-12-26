import numpy as np

a = np.array([1,3])
b = np.array([0,3])

# perkalian dot
c  = np.dot(a,b)

# perkalian cross
a = np.array([1,2,0])
b = np.array([2,1,0])

c = np.cross(a,b)
c2 = np.cross(b,a)


print (c)
print (c2)