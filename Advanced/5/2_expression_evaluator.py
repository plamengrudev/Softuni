from collections import deque

expression=input().split()
result=deque()

operations={
    "+": lambda a,b:a+b,
    "-": lambda a,b:a-b,
    "*": lambda a,b:a*b,
    "/": lambda a,b:a//b
}

for char in expression:
    if char not in "+-*/":
        result.append(int(char))
    else:
        while len(result)>1:
            first_num=result.popleft()
            second_num=result.popleft()
            result.appendleft(operations[char](first_num,second_num))

print(result[0])
