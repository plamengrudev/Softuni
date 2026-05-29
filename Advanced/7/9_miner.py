n=int(input())
matrix=[]
start=[]
position=[]
coal_left=0
game_over=False

commands=[x for x in input().split()]
for _ in range(n):
    matrix.append([x for x in input().split()])

operations={
    "left": lambda x,y: (x,y-1) if 0<=y-1<n else (x,y),
    "right": lambda x,y: (x,y+1) if 0<=y+1<n else (x,y),
    "up": lambda x,y: (x-1,y) if 0<=x-1<n else (x,y),
    "down": lambda x,y: (x+1,y) if 0<=x+1<n else (x,y)
}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='s':
            start=[i,j]
        if matrix[i][j]=='c':
            coal_left+=1
position=start
for direction in commands:
    position=operations[direction](*position)
    r,w=position
    if matrix[r][w]=='c':
        if coal_left-1==0:
            print(f"You collected all coal! ({r}, {w})")
            coal_left-=1
            game_over=True
            break
        else:
            coal_left-=1
            matrix[r][w]='*'
    elif matrix[r][w]=='e':
        print(f"Game over! ({r}, {w})")
        game_over=True
        break

if not game_over:
    print(f"{coal_left} pieces of coal left. ({', '.join(map(str,position))})")
    
    

