n=int(input())
matrix=[[x for x in input().split()] for _ in range(n)]
start=[]
bags=0
is_dead=False

operations={
		"up": lambda row, col: (row - 1, col),
		"down": lambda row, col: (row + 1, col),
		"left": lambda row, col: (row, col - 1),
		"right": lambda row, col: (row, col + 1),
	}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='A':
            start=[i,j]
            matrix[i][j]='*'
nr,nc=start
while True:
    if not is_dead and bags<10:
        command=input()
        nr,nc=operations[command](nr,nc)
        if 0<=nr<n and 0<=nc<n and bags<10:
            if matrix[nr][nc]=='.':
                matrix[nr][nc]='*'
            elif matrix[nr][nc]=='R':
                matrix[nr][nc]='*'
                is_dead=True
                break
            elif matrix[nr][nc]=='*':
                continue
            else:
                bags+=int(matrix[nr][nc])
                matrix[nr][nc]='*'
        else:
            is_dead=True
            break

    else:
        break

if is_dead:
    print(f"Alice didn't make it to the tea party.")
    for i in range(len(matrix)):
        print(*matrix[i])
if not is_dead and bags>=10:
    print(f"She did it! She went to the party.")
    for i in range(len(matrix)):
        print(*matrix[i])



