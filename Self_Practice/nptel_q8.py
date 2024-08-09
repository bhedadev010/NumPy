#Create a Python program that takes a list of integers, reverses the list, adds the
# values at odd indices from both the original and reversed lists, and creates a new
# list with the result. The new list should be printed in the end.

n = "1 5 4 6 7 4 5 3"
li = n.split(" ")
l = list()
for i in li:
    l.append(int(i))
a = l[::-1]
print(l)
print(a)
m = list()

for i in range(0,len(a)):
    if i%2==0:
        m.append(l[i])
    else:
        m.append(a[i]+l[i])
for i in m:
    print(i,end=" ")