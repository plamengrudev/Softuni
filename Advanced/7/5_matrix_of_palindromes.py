rows,columns=[int(x) for x in input().split()]
matrix=[]
start=ord('a')

for i in range(rows):
        matrix.append([chr(start+int(i))+chr(start+int(i+j))+chr(start+int(i)) for j in range(columns)])

print(*[' '.join(row) for row in matrix],sep='\n')