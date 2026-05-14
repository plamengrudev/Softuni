text=input().split()
stack=[]
while len(text) >0:
    stack.append(text.pop())
print(" ".join(stack))