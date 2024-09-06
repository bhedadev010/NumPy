import re

filename = input("Enter the filename :")
filename = filename + ".txt"
with open(filename,"r") as file:
    file = file.read()
    numbers = re.findall(r'\d+', file)

    print(numbers)
