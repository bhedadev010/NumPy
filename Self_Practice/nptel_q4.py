n = 10294343763482 *(10**2309)
k = 0
a = []
b = 0
while(n !=0):
    k = k + (n % 10)
    a.append(n % 10)
    n = n//10
a.sort()
for i in a:
    b = b+i
if(b==k):
    print("we know")
else:
    print("we are")
print(k)
print(b)