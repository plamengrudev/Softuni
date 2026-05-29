rows,columns=[int(x) for x in input().split()]
matrix=[]
count=0

for _ in range(rows):
    matrix.append([x for x in input().split()])

for i in range(len(matrix)-1):
    for j in range(len(matrix[i])-1):
        if matrix[i][j]==matrix[i+1][j]==matrix[i+1][j+1]==matrix[i][j+1]:
            count+=1

print(count)