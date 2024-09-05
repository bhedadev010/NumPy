import numpy as np

# Slicing Sub-Arrays:
#
# Given a 3D array of shape (5, 5, 5), extract:
# A 3x3x3 sub-array from the middle of the original array.
# All elements from the first two layers and first three rows of the array.

a = np.random.randint(1, 100, (5, 5, 5))

print(a)

print(a[1:4,1:4,1:4])
print(a[0:2,0:3])


# Manipulating Specific Elements:
#
# Create a 3D array of shape (3, 3, 3) where each element is equal to its index sum (i + j + k).
# Extract:
# All elements from the array that have an index sum divisible by 2.

b = np.fromfunction(lambda i, j, k: i + j + k, (3, 3, 3), dtype=int)

print(b)
print(b[b%2==0])


# Replacing Specific Elements:
#
# Given a 4x4x4 array of random integers, replace all elements in the
# last layer with their negative values.

a = np.random.randint(1, 100, (4, 4, 4))

print(a)

a[-1, :, :] = -a[-1, :, :]
print(a)