# Create a NumPy array of size (4, 5) filled with random integers between 1 and 100.
#
# Use the .size attribute to find the total number of elements in the array and the .dtype
# attribute to find its data type.
#
# Calculate the total memory used by the array (Hint: Use .itemsize to find the size of
# each element in bytes).

import numpy as np


a = np.random.randint(1,101,size=(3,4))
print(a)
print(a.size)
print(a.dtype)
print(a.itemsize)
print("total size : ",a.size*a.itemsize)
print("*"*40)


# Create a NumPy array containing the following floating-point numbers: [1.7, 2.8, 3.3, 4.9].
# Convert this array to integers using .astype(). What happens to the values after conversion?
# Convert the integer array back to float64 and verify its data type.

a = np.array([1.7, 2.8, 3.3, 4.9])
print(a)
a = a.astype('int64')
print(a.dtype)
print(a)
a = a.astype('float64')
print(a.dtype)