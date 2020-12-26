import numpy as np

# membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]),dtype = float)

# membuat matrix dengan menggunankan functions
def kuadrat(baris, kolom):
  return kolom**2
  
def jumlah(baris, kolom):
  return (baris + kolom)

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)


# membuat matrix atau array dengan iterable

iterable = (x*4 for x in range(5))

d = np.fromiter(iterable, dtype = int)

#  multidimensi array
dtipe = [('nama','5255'),('tinggi',int)]

data = [
  ['ucup',150],
  ['otong',160],
  ['ipul',180]
  ]

e = np.array(data, dtype = dtipe)

print (e)