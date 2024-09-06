filename = input("Enter file name :")
filename = filename + ".txt"
with open(filename,"r") as file:
    file = file.read()
    lene = file.split()
    print(lene)
    for i in lene:
        if(len(i)== 4):
            lene[lene.index(i)] = "****"
print(lene)
