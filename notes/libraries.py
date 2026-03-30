# GNB - 1st - Libraries Notes
import numpy as np

#print(np.__version__)

a = np.arange(15).reshape(3, 5)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = np.array([6, 7, 8])
print(type(b))