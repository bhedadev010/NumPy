import numpy as np

# Masking Elements:
#
# Create a 7x7 matrix of integers from 1 to 49. Extract all elements that are divisible by 3.

a = np.random.randint(1,50,(7,7))
print(a)

print(a[a%3==0])

# Extracting Planes:
#
# Given a 3D array of shape (4, 4, 4), extract:
# The 2D plane formed by the third layer.
# The diagonal elements from the first layer.
# The last two layers of the array.

a = np.random.randint(1, 100, (4, 4, 4))
print(a)

print(a[2])
print(a[0,[0,1,2,3],[0,1,2,3]])
print(a[2:])