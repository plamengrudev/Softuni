first=set([int(x) for x in input().split()])
second=set([int(x) for x in input().split()])

N=int(input())

def append_to(pos,list):
    if pos=="First":
        for n in list[2:]:
            first.add(int(n))
    elif pos=="Second":
        for n in list[2:]:
            second.add(int(n))

def remove_from(pos,list):
    if pos=="First":
        for n in list[2:]:
            if int(n) in first:
                first.remove(int(n))
    elif pos=="Second":
        for n in list[2:]:
            if int(n) in second:
                second.remove(int(n))

for _ in range(N):
    arg_p=[x for x in input().split()]
    command, position=arg_p[0],arg_p[1]
    if command=="Add":
         append_to(position,arg_p)
    elif command=="Remove":
        remove_from(position,arg_p)
    elif command=="Check":
        if first.issubset(second) or second.issubset(first):
            print(f"True")
        else:
            print(f"False")

print(f"{', '.join(map(str,sorted(first)))}")
print(f"{', '.join(map(str,sorted(second)))}")