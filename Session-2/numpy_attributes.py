import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],[4,5.0,6]])
arr_3d = np.array([[[1,2,4],[4,"wow",6.0]],[[1,'a',3],[4,5,6]]])

# 1) arr.shape() = returns the structure of array given
print(arr_1d.shape)
print(arr_2d.shape)
print(arr_3d.shape)

# 2) arr.ndim = returns the dimension of the array
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

# 3) arr.size = returns the number of elements present in array
print(arr_1d.size)
print(arr_2d.size)
print(arr_3d.size)

# 4) arr.dtype = returns the datatype of elements present in array
print(arr_1d.dtype)
print(arr_2d.dtype)
print(arr_3d.dtype)

# 5) arr.astype = changes the datatype of an numpy array
a = arr_1d.astype('float64')
print(a)
a = arr_1d.astype('int64')
print(a)