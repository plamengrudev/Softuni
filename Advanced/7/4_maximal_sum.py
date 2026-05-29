rows,columns=[int(x) for x in input().split()]
matrix=[]
selected=[]
summ=float("-inf")
max_row,max_col=0,0

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for i in range(rows-2):
    for j in range(columns-2):
        temp=0
        for r in range(i,i+3):
            for c in range(j,j+3):
                temp+=matrix[r][c]
        
        if temp>summ:
            summ=temp
            max_row=i
            max_col=j

print(f"Sum = {summ}")
for i in range(max_row,max_row+3):
    print(*[matrix[i][x] for x in range(max_col,max_col+3)])
