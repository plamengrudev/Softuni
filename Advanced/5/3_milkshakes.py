from collections import deque

chocolates=[int(x) for x in input().split(", ")]
cups=deque([int(x) for x in input().split(", ")])
milkshakes=0

while milkshakes<=5:
    if milkshakes==5:
        print(f"Great! You made all the chocolate milkshakes needed!")
        break
    if chocolates and chocolates[-1]<=0:
        chocolates.pop()
        continue
    if cups and cups[0]<=0:
        cups.popleft()
        continue
    if cups and chocolates:
        if cups[0]==chocolates[-1]:
            milkshakes+=1
            cups.popleft()
            chocolates.pop()
        else:
            cups.rotate(-1)
            chocolates[-1]-=5
    else:
        print(f"Not enough milkshakes.")
        break

if chocolates:
    print(f"Chocolate: {', '.join(map(str,chocolates))}")
else:
    print(f"Chocolate: empty")

if cups:
    print(f"Milk: {', '.join(map(str,cups))}")
else:
    print(f"Milk: empty")