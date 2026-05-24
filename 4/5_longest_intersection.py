count=int(input())
longest=[]


for _ in range(count):
    a_set=set()
    b_set=set()
    ranges=[x for x in input().split("-")]
    a=[int(x) for x in ranges[0].split(",")]
    b=[int(x) for x in ranges[1].split(",")]
    for i in range(a[0],a[1]+1):
        a_set.add(i)
    for i in range(b[0],b[1]+1):
        b_set.add(i)
    if len(longest)<len(a_set & b_set):
        longest=(a_set & b_set)

print(f"Longest intersection is {list(longest)} with length {len(longest)}")