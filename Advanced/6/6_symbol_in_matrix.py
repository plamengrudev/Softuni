n=int(input())
matrix=[]
is_found=False

for _ in range(n):
    matrix.append([x for x in input()])

symbol=input()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==symbol:
            print(f"({i}, {j})")
            is_found=True
            break
    if is_found:
        break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
