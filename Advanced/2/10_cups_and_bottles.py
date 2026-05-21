from collections import deque

cups=deque([int(x) for x in input().split()])
bottles=[int(x) for x in input().split()]
wasted_water=0

while list(cups):
    if bottles:
        if bottles[-1]>=cups[0]:
            wasted_water+=bottles[-1]-cups[0]
            cups.popleft()
            bottles.pop()
        elif bottles[-1]<cups[0]:
            cups[0]=cups[0]-bottles[-1]
            bottles.pop()
    else:
        break

if cups:
    print(f"Cups: {' '.join(map(str,cups))}")
else:
    print(f"Bottles: {' '.join(map(str,reversed(bottles)))}")

print(f"Wasted litters of water: {wasted_water}")


