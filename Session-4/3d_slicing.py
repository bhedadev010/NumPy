import numpy as np

a = np.arange(1,46).reshape(3,3,5)
print(a)

print(a[0:2,0::,0])

print(a[0::2,1::,3::])

print(a[0:2,1,1:4])

print(a[1:,0::2,-2:])