# Create a 2D array with 4 rows and 5 columns filled with zeros.
# Change its shape to a 1D array with 20 elements using the .reshape() method.
# Verify the number of dimensions and size of the new array using .ndim and .size.

import numpy as np

a = np.zeros(shape=(4,5))
print(a)
a = a.reshape(a.size)
print(a)
print(a.ndim, a.size)


# Create an array of 8 random integers between 1 and 50.
# Convert this array to str type using .astype().
# Check the data type and then convert it back to integers. Explain if any changes occur in the values.

a = np.random.randint(1,51,size=8)
print(a)
a = a.astype('str')
print(a)
a = a.astype('i')
print(a)