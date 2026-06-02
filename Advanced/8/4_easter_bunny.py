n=int(input())
matrix=[[x for x in input().split()] for _ in range(n)]
start=[]
path=[]
sum=float('-inf')
best_direction=None


operations={
    'up': (-1,0),
    'down': (1,0),
    'left': (0,-1),
    'right': (0,1)
}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='B':
            start=[i,j]


for direction,move in operations.items():
    temp_sum=0
    temp_path=[]
    row_change,col_change=move
    nr=start[0]+int(row_change)
    nc=start[1]+int(col_change)

    while 0<=nr<n and 0<=nc<n and matrix[nr][nc]!='X':
        temp_sum+=int(matrix[nr][nc])
        temp_path.append([nr,nc])
        nr+=int(row_change)
        nc+=int(col_change)
    if temp_sum>sum and len(temp_path)>0:
        best_direction=direction
        path=temp_path
        sum=temp_sum

print(best_direction)
for i in range(len(path)):
    print(path[i])
print(sum)



