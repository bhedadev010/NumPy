#Create a Python program that removes all duplicate positive integer numbers(includes zero)
# from a list and prints the unique numbers in the order they first appeared.
#The program should prompt the user to input a list of numbers, then process the list
# to remove duplicates and print the resulting list of unique numbers.

m = input()
m = m.split(" ")
n = list()
for i in m:
    n.append(int(i))

uni = list()

for i in range(0,len(n)):
    if n[i] not in uni:
        uni.append(n[i])

for i in uni:
    print(i,end=" ")