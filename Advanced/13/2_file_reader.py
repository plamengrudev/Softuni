result=[]
try:
    with open('numbers.txt','r') as f:
        for num in f:
            result.append(int(num))
    print(sum(result))
except FileNotFoundError:
    pass