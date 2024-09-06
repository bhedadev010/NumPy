filename = input("Enter the filename :")
filename = filename + ".txt"
with open(filename,"r") as file:
    file = file.read()
    lene = file.split()
    for i in lene:
        print(i)
        if(len(i)== 4):
            lene[i] = "****"

    print(file)

