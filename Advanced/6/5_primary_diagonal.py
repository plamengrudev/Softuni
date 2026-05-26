rows=int(input())
matrix=[]
sum=0

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(len(matrix)):
    sum+=matrix[i][i]

print(sum)