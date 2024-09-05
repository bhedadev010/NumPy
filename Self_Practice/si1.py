import numpy as np

# Extracting Rows and Columns:
#
# Given a 5x5 matrix of integers, extract:
# All elements from the second row.
# The first three elements of the fourth column.
# Every alternate element from the first row.

m = np.array([[1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]])

print(m[1])
print(m[3,0:3])
print(m[0,1::2])


# Extracting Sub-matrices:
#
# Given a 6x6 matrix of random numbers, extract:
# A 3x3 sub-matrix from the top-left corner.
# A 2x2 sub-matrix from the center of the matrix.
# All the elements in the last two columns

n = np.random.randint(1, 100, (6, 6))

print(n)
print(n[0:3,0:3])

print(n[2:4,2:4])
print(n[4:])