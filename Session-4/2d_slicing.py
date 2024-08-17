import numpy as np

a = np.arange(1,26).reshape((5,5))
print(a)

print(a[0])

print(a[0::2])

print(a[1::2])

print(a[0,0::2])

print(a[2::,0:2])

print(a[0::,3])

print(a[1:4:,1:4])