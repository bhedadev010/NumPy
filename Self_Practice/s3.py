# Create a NumPy array arr = np.array([0, 1, 0, 1, 1, 0, 1]).
# Convert this array to a boolean type using .astype().
# Use the .shape and .ndim attributes to find the shape and the
# number of dimensions of this boolean array.

import numpy as np

arr = np.array([0, 1, 0, 1, 1, 0, 1])
arr.astype('b')
print(arr)
print(arr.shape)
print(arr.ndim)
print("*"*40)


# Given an array arr = np.array([[10, 20], [30, 40], [50, 60]], dtype=np.int32),
# use .dtype to find the data type of the array.
# Convert the array to float64 and then check the data type again using .dtype.

arr = np.array([[10, 20], [30, 40], [50, 60]], dtype=np.int32)
print(arr.dtype)
arr = arr.astype('float64')
print(arr.dtype)
print(arr)


# Create a 3D NumPy array with shape (2, 3, 4) filled with random
# floating-point numbers between 0 and 1.
#
# Use .astype() to convert it to float32.
#
# Find and print its shape, number of dimensions, size, and data type.

a = np.random.random(size=(2,3,4))
print(a)
a = a.astype('float32')
print(a.dtype)
print(a.shape, a.ndim, a.size)