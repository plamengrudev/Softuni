rows, columns=[int(x) for x in input().split(', ')]
matrix=[]
sum=0
result=[[0 for x in range(2)] for y in range(2)]

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(len(matrix)-1):
    for j in range(len(matrix[i])):
        if j+1<len(matrix[i]):
            temp=matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1]
            if temp>sum:
                sum=temp
                result[0][0]=matrix[i][j]
                result[0][1]=matrix[i][j+1]
                result[1][0]=matrix[i+1][j]
                result[1][1]=matrix[i+1][j+1]
for i in range(len(result)):
    print(f"{' '.join(map(str,result[i]))}")
print(sum)


# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0