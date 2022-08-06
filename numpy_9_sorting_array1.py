import numpy as np

x = np.floor(np.random.randn(1,6)*10)

print (x)
print ("nilai max dari x adalah = ",x.max())
print ("posisi max dari x adalah = ",x.argmax())
print ("nilai min dari x adalah = ",x.min())
print ("posisi min dari x adalah = ",x.argmin())

print ("mengurutkan nilai x:")
print (np.sort(x))
print (np.argsort(x))
