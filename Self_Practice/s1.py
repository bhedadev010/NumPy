#Create a NumPy array of integers from 1 to 10. Convert this
#array to type float32 using the .astype() method.
#Print the new array and its data type.

import numpy as np
import random

a = np.arange(1,11)
print(a)
a = a.astype('float32')
print(a)
print(a.dtype)
print("*"*40)


# Given the array arr = np.array([[1, 2, 3], [4, 5, 6]]), use the .ndim
# and .shape attributes to find the number of dimensions and the shape of the array.
# What are the results?

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)
print(arr.shape)
print("*"*40)


# Create a 1D array of 12 elements (values ranging from 1 to 12).
# Reshape this array into a 2D array with 3 rows and 4 columns using the .reshape() method.
# What is the shape of the new array?

a = np.arange(1,13).reshape(3,4)
print(a.shape)