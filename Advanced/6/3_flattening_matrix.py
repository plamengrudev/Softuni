rows=int(input())
array=[]
matrix=[]

for i in range(rows):
    array.append([int(x) for x in input().split(', ')])

for i in range(len(array)):
    for j in range(len(array[i])):
        matrix.append(array[i][j])

print(matrix)