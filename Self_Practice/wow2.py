alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

filename = input("Enter the filename :")
filename = filename + ".txt"
with open(filename,"r") as file:
    content = file.read()
    content = content.lower()

dict1 = {}

for i in alpha_list:
    counter = 0
    for j in content:
        if (j == i):
            counter +=1

    dict1[i] = counter

print(dict1)





