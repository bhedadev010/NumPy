import math

a = 8

def omg(a):
    if a < 2:
        return False

    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

if omg(a):
    print('wow')
else:
    print("boo")
