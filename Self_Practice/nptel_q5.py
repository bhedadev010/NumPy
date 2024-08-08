#Create a Python program that finds the second largest number in a list of positive
# integers(includes zero). The program should prompt the user to input a list of
# numbers, then compute and print the second largest number in that list.

n = "1 5 4 6 7 4 5 3"
li = n.split(" ")
l = list()
for i in li:
    l.append(int(i))
l.sort(reverse=True)
print(l)
a = 0
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        a = l[i+1]
        break
print(a)