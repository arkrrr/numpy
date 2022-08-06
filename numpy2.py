import numpy as np

# meembuat vector 
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,6,8])

# membuuat vector dengan range
c = np.arange(1,10,2)

# membuat linspace
d = np.linspace(1,12,6)

#  array multidimensi / matriks
e = np.array([(1,2,3), (4,5,6) ])

# matriks dengan nilai nol
f = np.zeros((5,5))

# matriks dengan nilai satu
g = np.ones((5,5))

# matriks identitas
h1 = np.identity(8)
h2 = np.eye(10)
# display
print (h1)
