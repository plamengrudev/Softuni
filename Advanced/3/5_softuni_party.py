count=int(input())
codes=set()

for _ in range(count):
    codes.add(input())

while True:
    guest=input()
    if guest=="END":
        print(len(codes))
        vip=[x for x in codes if x[0].isdigit()]
        regular=[x for x in codes if x[0].isalpha()]
        for item in sorted(vip):
            print(item)
        for item in sorted(regular):
            print(item)
        break
    elif guest in codes:
        codes.remove(guest)
