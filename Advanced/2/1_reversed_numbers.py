text=list(input())

for _ in range(len(text)):
    print(f"{text.pop()}",end="")