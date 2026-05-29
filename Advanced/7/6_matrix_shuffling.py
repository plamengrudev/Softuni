rows, cols=[int(x) for x in input().split()]
matrix=[[x for x in input().split()] for _ in range(rows)]

def check_is_valid_coords(a,b):
    return a in range(rows) and b in range(cols)



while True:
    line=input()
    if line=="END":
        break
    parts=line.split()
    if "swap"==parts[0] and all(ele.isdigit() for ele in parts[1:]):
        command, *args = [x if i == 0 else int(x) for i, x in enumerate(line.split())]
        if check_is_valid_coords(args[0],args[1]) and check_is_valid_coords(args[2],args[3]) and len(args)==4:
            matrix[args[0]][args[1]],matrix[args[2]][args[3]]=matrix[args[2]][args[3]],matrix[args[0]][args[1]]
            print(*[' '.join(x) for x in matrix],sep='\n')
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
