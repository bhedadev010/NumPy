import numpy as np
import random

# np.round()
arr = np.random.random((2,3))
arr = np.round(arr*100)
print(arr)

# np.sum()
    #axis=0 => column
print(np.sum(arr,axis=0))
    #axis=1 => row
print(np.sum(arr,axis=1))

# np.prod()
    #axis=0 => column
print(np.prod(arr,axis=0))
    #axis=1 => row
print(np.prod(arr,axis=1))

print(np.max(arr))

print(np.min(arr))