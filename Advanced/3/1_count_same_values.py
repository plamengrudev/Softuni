tup=tuple(float(x) for x in input().split())
checked=[]
for t in tup:
    if t in checked:
        continue
    else:
        print(f"{t:.1f} - {tup.count(t)} times")
        checked.append(t)