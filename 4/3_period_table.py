count=int(input())

elements=set()

for _ in range(count):
    elements.update([x for x in input().split()])

for el in elements:
    print(el)