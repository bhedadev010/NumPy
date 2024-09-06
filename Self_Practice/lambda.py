#lambda function is an anonymous function which can be defined in a single line of code without name.
#a name

a = lambda x,y:x**y
print(a(2,3))

b = [1,2,3,4,5]
c = list(filter(lambda d:d**2,b))
print(c)

d = list(filter(lambda x:x%2==0,b))
print(d)

s = lambda x:len(x)
print(s('dev'))

m = list(filter(lambda a:a%2==0,b))
print(m)

a = ['awow','aahggre','z']
b = sorted(a,key=lambda a:len(a))
print(b)


w = {'abc':100,'b':20,'c':19}
a = max(w,key=lambda a:w[a])
print(a)