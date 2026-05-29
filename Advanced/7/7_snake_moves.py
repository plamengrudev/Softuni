from collections import deque
rows,cols=[int(x) for x in input().split()]
line=deque(input())
matrix=[]

for row in range(rows):
    matrix.append([""]*cols)
    for col in range(cols):
        if row%2==0:
            matrix[row][col]=line[0]
        else:
            matrix[row][-1-col]=line[0]
        line.rotate(-1)
    print(*matrix[row],sep='')
