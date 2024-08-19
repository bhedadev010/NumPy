n = int(input())
matrix = []

for i in range(n):
    row = []
    elements = input().split()
    for element in elements:
        row.append(int(element))
    matrix.append(row)

skew = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != -matrix[j][i]:
            skew = False
            break
    if not skew:
        break

if skew:
    print(1)
else:
    print(0)
