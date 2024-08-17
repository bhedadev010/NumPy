import numpy as np

a = np.arange(1,46).reshape(3,3,5)
print(a)

print(a.shape)

print(a[0][0][4])

print(a[0][2][2])

print(a[1][1][0])

print(a[1][2][3])

print(a[2][1][2])