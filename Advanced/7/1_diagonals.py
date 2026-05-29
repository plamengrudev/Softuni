n=int(input())
matrix=[]
primary=[]
secondary=[]

for _ in range(n):
    matrix.append([int(x) for x in input().split(', ')])


primary = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row])) if row == col]
secondary = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[row])) if row + col == len(matrix) - 1]

print(f"Primary diagonal: {', '.join(map(str,primary))}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(map(str,secondary))}. Sum: {sum(secondary)}")