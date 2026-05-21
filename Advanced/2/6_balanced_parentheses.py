from collections import deque
chars=deque([x for x in input()])
stack=[]
opening=['{','[','(']
closing=['}',']',')']

is_balanced=True

while len(chars)>0:
    item=chars.popleft()
    if item in opening:
        stack.append(item)
    elif item in closing:
        if len(stack)==0:
            is_balanced=False
            break
        elif opening.index(stack[-1])==closing.index(item):
            stack.pop()
        else:
            is_balanced=False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
            
