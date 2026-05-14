text=input()
indexes=[]

for i in range(len(text)):
    if text[i]=="(":
        indexes.append(i)
    elif text[i]==")":
        start_idx=indexes.pop()
        print(text[start_idx:i+1])