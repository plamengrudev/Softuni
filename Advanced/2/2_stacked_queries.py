input_int=int(input())
stack=[]
for _ in range(input_int):
    args=input().split()
    if len(args)==1:
        if args[0]=="2":
            if stack:
                stack.pop()
        elif args[0]=="3":
            if stack:
                print(max(stack))
        elif args[0]=="4":
            if stack:   
                print(min(stack))
    else:
        stack.append(int(args[1]))

remaining=[]
for _ in range(len(stack)):
    remaining.append(str(stack.pop()))
print(", ".join(remaining))