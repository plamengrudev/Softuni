stack=[int(x) for x in input().split()]
capacity=int(input())
count=1
temp=0

while len(stack)>0:
    
    if stack[-1]+temp<=capacity:
        temp+=stack.pop()
    elif stack[-1]+temp>capacity:
        count+=1
        temp=stack.pop()
print(count)