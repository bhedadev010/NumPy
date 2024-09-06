def mea(n):
    if len(n)==0:
        return -1
    ele = len(n)
    tot = sum(n)
    return tot/ele

a = [1,2,3,4,5,6,7,89]
res = mea(a)
print(res)