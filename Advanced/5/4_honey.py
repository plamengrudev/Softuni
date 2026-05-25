from collections import deque

worker_bees=deque([int(x) for x in input().split()])
nectar=[int(x) for x in input().split()]
symbols=deque(input().split())
honey=0

operations={
    "+": lambda a,b: abs(a+b),
    "-": lambda a,b: abs(a-b),
    "*": lambda a,b: abs(a*b),
    "/": lambda a,b: abs(a/b) if b!=0 else 0
}


while worker_bees and nectar:
    if nectar[-1]>=worker_bees[0]:
        honey+=operations[symbols[0]](worker_bees[0],nectar[-1])
        nectar.pop()
        worker_bees.popleft()
        symbols.popleft()
    else:
        nectar.pop()



print(f"Total honey made: {honey}")

if worker_bees:
    print(f"Bees left: {', '.join(map(str,worker_bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str,nectar))}")

