sze=int(input())
matrix=[]
primary=[]
secondary=[]


for _ in range(sze):
    matrix.append([int(x) for x in input().split(" ")])

primary=[matrix[x][x] for x in range(len(matrix))]
secondary=[matrix[x][len(matrix)-x-1] for x in range(len(matrix))]

print(abs(sum(primary)-sum(secondary)))
