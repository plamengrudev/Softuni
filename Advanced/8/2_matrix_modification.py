n=int(input())
matrix=[[int(x) for x in input().split()] for _ in range(n)]

while True:
    line=input()
    if line=="END":
        for i in range(len(matrix)):
            print(*matrix[i])
        break
    else:
        command, *args = line.split()
        args = [int(x) for x in args]
        if 0<=args[0]<n and 0<=args[1]<n:
            if command=="Add":
                matrix[args[0]][args[1]]+=int(args[2])
            elif command=="Subtract":
                matrix[args[0]][args[1]]-=int(args[2])
        else:
            print("Invalid coordinates")