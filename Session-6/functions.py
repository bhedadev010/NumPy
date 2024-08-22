#Return a sorted copy of an array

import numpy as np
a = np.random.randint(1,100,15)
print(np.sort(a))
print(np.sort(a)[::-1])

#appends values along the mentioned axis at the end of the array

a = np.array([1,2,3])
print(np.append(a,4))
a = [[1,2,3,4]]

b = np.random.rand(2,4)
print(np.append(a,b,axis=0))

#function concatenate a sequence of arrays along an existing axis.

c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)
print(np.concatenate((c,d),axis=1))

# we can get the unique values from an array given as parameter in np.unique() method.

e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(np.unique(e))

# we can get the expanded dimensions of an array

print(np.shape(e))
print(np.expand_dims(e,axis=0))
print(np.expand_dims(e,axis=1))


#eturns the indices of elements in an input array where the given condition is satisfied.

# replace all values > 50 with 0
a = np.array([18, 86, 27, 73, 61, 40, 21, 36, 84, 43, 58,  3, 94, 52, 47])
print(a)
print(np.where(a>50,0,a))

#returns indices of the max/min element of the array in a particular axis.

a=np.array([18, 86, 27, 73, 61, 40, 21, 36, 84, 43, 58,  3, 94, 52, 47])
print(np.argmax(a))
print(np.argmin(a))

#cumulative sum of array elements over a given axis

print(np.cumsum(a))
print(np.cumprod(a))

#compute the nth percentile of the given data

print(np.sort(a))
print(np.percentile(a,80))

#function which represents the frequency of data distribution

print(np.histogram(a,bins=[0,20,40,60,80,100]))

#Return Pearson product-moment correlation coefficients.

salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])

print(np.corrcoef(salary,experience))

# having values are checked in a different numpy array having different elements with different sizes.

items = [10,20,30,40,36,50,60,70,80,90,100]
print(a[np.isin(a,items)])
print(np.isin(a,items))

#reverses the order of array elements along the specified axis

print(a)
print(np.flip(a))

#function replaces specific elements of an array with given values

a = np.array([-44,   1, -55,   3,   4])
a = np.arange(5)
np.put(a, [0, 2], [-44, -55])
print(a)

#returns a new array with the deletion of sub-arrays along with the mentioned axis

a = np.array([10, 30, 13, 38, 87, 59, 30, 92, 74, 11, 18, 89, 72, 30, 94])
print(np.delete(a,[0,2,4]))

#union

m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

print(np.union1d(m,n))

#intersect

print(np.intersect1d(m,n))

#setdiff

print(np.setdiff1d(m,n))

#setxor

print(np.setxor1d(m,n))

#in1d find if present

print(m[np.in1d(m,5)])

#used to Clip (limit) the values in an array.

a = np.array([10, 30, 13, 38, 87, 59, 30, 92, 74, 11, 18, 89, 72, 30, 94])
print(np.clip(a,a_min=25,a_max=75))

#repeat elements

x = np.array([[1,2],[3,4]])
print(np.repeat(x, 2))
