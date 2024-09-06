f = open("text1.txt","a+")
list1 = [ "hey", "yehhh", "now"]

f.write("now \neverthing \nwill be in new line.\n")
f.seek(0)
print(f.read())
f.seek(0)
print(f.readlines())
f.writelines(line + "\n" for line in list1)
f.seek(0)
read1 = f.readlines()
len_of_lines = len(read1)
for line in read1:
    lines = line.split()
    lines = lines.split()

print(len_of_lines)
print(len_of_char)