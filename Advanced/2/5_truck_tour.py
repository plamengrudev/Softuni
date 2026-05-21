from collections import deque

num_pumps=int(input())
pumps=deque()

for i in range(num_pumps):
    inpts=input().split()
    fuel,distance=int(inpts[0]),int(inpts[1])
    pumps.append({"fuel":fuel,"distance":distance})
start_idx=0
stops=0
tank=0
while num_pumps>stops:
    for item in pumps:
        if item["fuel"]+tank>=item["distance"]:
            tank+=item["fuel"]-item["distance"]
            stops+=1
        else:
            pumps.rotate(-1)
            start_idx+=1
            stops=0
            tank=0
            break
print(start_idx)

