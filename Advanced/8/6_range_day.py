n=5

matrix=[[x for x in input().split()] for _ in range(n)]
commands=int(input())

start=[]
targets=[]

for i in range(n):
    for j in range(n):
        if matrix[i][j]=='A':
            start=[i,j]
        if matrix[i][j]=='x':
            targets.append([i,j])
position=list(start)
hit_targets=[]

aims={
    'up': lambda x,y: (x-1,y),
    'down': lambda x,y: (x+1,y),
    'left': lambda x,y: (x,y-1),
    'right': lambda x,y: (x,y+1)
    }


for i in range(commands):
    line=input().split()
    command=line[0]
    if command=="shoot":
        direction=line[1]
        temp_position=position
        while True:
            target=temp_position
            target=aims[direction](*target)
            r,c=target
            if 0<=r<n and 0<=c<n:
                if matrix[r][c]=='.':
                    temp_position=[r,c]
                elif matrix[r][c]=='x':
                    if [r,c] in targets:
                        targets.remove([r,c])
                    matrix[r][c]='.'
                    hit_targets.append([r,c])
                    break
                else:
                    break
            else:
                break
    if not targets:
        break

    elif command=="move":
        direction,moves=line[1],int(line[2])
        pr,pc=position
        if direction=='up':    nr,nc=pr-moves,pc
        elif direction=='down':  nr,nc=pr+moves,pc
        elif direction=='left':  nr,nc=pr,pc-moves
        elif direction=='right': nr,nc=pr,pc+moves
        if 0<=nr<n and 0<=nc<n and matrix[nr][nc]=='.':
            matrix[pr][pc]='.'
            matrix[nr][nc]='A'
            position=[nr,nc]

if targets:
    print(f"Training not completed! {len(targets)} targets left.")
    for i in range(len(hit_targets)):
        print(hit_targets[i])
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
    for i in range(len(hit_targets)):
        print(hit_targets[i])
    


# . . . . . 
# x . . . . 
# . A . . . 
# . . . x . 
# . x . . x 
# 2
# move right 4
# move left 1