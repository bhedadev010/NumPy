import numpy as np

a = np.zeros((3,4),dtype='i')
print(a)

a1 = np.array([1,2,3,4,5,6,7])
print(a1)
a2 = a1.view()
print(a2)
a1[0] = 7
print(a1,a2)
a2[0]=3
print(a1,a2)