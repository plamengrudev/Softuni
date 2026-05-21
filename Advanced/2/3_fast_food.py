from collections import deque

food=int(input())
queue=deque(int(x) for x in input().split())

print(max(queue))
while len(queue)>0:
    if queue[0]>food:
        print(f"Orders left: {' '.join(map(str,queue))}")
        break
    else:
        food-=queue.popleft()
if len(queue)==0:
    print(f"Orders complete")