import numpy as np

arr = np.arange(0,50).reshape(5,10)
print(arr)

print(arr[arr%2==0])

print(arr[(arr%2==0) & (arr>40)])