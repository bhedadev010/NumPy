ms = list()
def magic_square(n):
    l = list()
    for i in range(3):
        l = []
        for j in range(3):
            l.append(0)
        ms.append(l)
    print(ms)

    i = n//2
    j = n-1

    num = n*n
    count = 1

    while count<=num:
        if i==-1 and j==n:
            j = n-2
            i=0
        else:
            if j==n:
                j=0
            if i<0:
                i=n-1
        if ms[i][j]!=0:
            j=j-2
            i=i+1
            continue
        else:
            ms[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(ms[i][j],end=" ")
        print()

magic_square(3)
