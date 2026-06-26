n=int(input())
grid=[]
for i in range(n):
    grid.append([x for x in input()])

total_treasure_avail=0
collected_treasure=0
durability=100
starting_point=[]
last_pos=[]
charm_landed=False

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=='*':
            total_treasure_avail+=1
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]=='S':
            starting_point=[i,j]
            break
operations={
    "left": lambda x, y: (x, (y - 1) % n),
    "right": lambda x, y: (x, (y + 1) % n),
    "up": lambda x, y: ((x - 1) % n, y),
    "down": lambda x, y: ((x + 1) % n, y)
}

position=starting_point
while True:
    if durability<=0:
        print(f"Shipwreck! Last known coordinates ({position[0]}, {position[1]})")
        break
    command=input()
    if command=='stop':
        print(f"Retreat! Some treasures remain unclaimed.")
        break
    else:
        direction=command
        last_pos=position
        grid[last_pos[0]][last_pos[1]]='.'
        position=operations[direction](*position)
        r,w=position
        if grid[r][w]=='*':
            if total_treasure_avail-1==0:
                print("Yo-ho-ho! All treasure chests collected!")
                total_treasure_avail-=1
                grid[r][w]='S'
                break
            else:
                total_treasure_avail-=1
                grid[r][w]='S'
        elif grid[r][w]=='M':
            durability-=25
            grid[r][w]='S'
        elif grid[r][w]=='C':
            if not charm_landed:
                durability+=25
                charm_landed=True
                if durability>100:
                    durability=100
            grid[r][w]='S'
        elif grid[r][w]=='.':
            grid[r][w]='S'
            

print(f"Ship Durability: {durability}")
if total_treasure_avail>0:
    print(f"Unclaimed chests: {total_treasure_avail}")

for i in range(n):
    print(f"{''.join(grid[i])}")
        