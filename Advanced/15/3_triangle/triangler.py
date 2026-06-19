def create(n: int):
    result=[]
    for i in range(1,n+1):
        result.append(i)
        print(' '.join(map(str,result)))
    for j in range(n,0,-1):
        result.pop()
        print(' '.join(map(str,result)))
