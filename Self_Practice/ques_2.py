import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

print(a[(a>=5) & (a<=10)])
print(a[np.where((a >= 5) & (a <= 10))])
