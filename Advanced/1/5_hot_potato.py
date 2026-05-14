from collections import deque

names=deque([x for x in input().split()])
tosses=int(input())

while len(names) > 1:
    names.rotate(-tosses+1)
    print(f"Removed {names.popleft()}")

print(f"Last is {names.pop()}")