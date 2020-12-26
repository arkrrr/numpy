import numpy as np

a = np.floor(np.random.randn(1,6)*10)

print (a)
print ("nilai max dari a adalah = ",a.max())
print ("posisi max dari a adalah = ",a.argmax())
print ("nilai min dari a adalah = ",a.min())
print ("posisi min dari a adalah = ",a.argmin())

print ("mengurutkan nilai a:")
print (np.sort(a))
print (np.argsort(a))