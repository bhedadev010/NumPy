def mystery(container):
    result = []
    for i in range(len(container)):
        if i % 2 == 0:
            result.append(container[i]*2)
        else:
            result.append(container[i]+3)
    return result

print(mystery([1,2,3,4,5,6,7,8,9]))