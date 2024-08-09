o = '1 0'
o = o.split(' ')
print(o)
m = list()
for i in o:
    m.append(int(i))
n = m[::-1]


if n == m:
    print("palindrome")
else:
    print("no")
