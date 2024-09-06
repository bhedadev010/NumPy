
def a(m,n):
    if m==0:
        return n
    return a(n%m,m)

m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))

result = a(m, n)
print(f"The GCD of {m} and {n} is: {result}")