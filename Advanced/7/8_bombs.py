n = int(input())
matrix = []
alive=0
sum=0
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs = [list(map(int, item.split(','))) for item in input().split()]

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

for row, col in bombs:
    if matrix[row][col] > 0:
        bomb = matrix[row][col]
        matrix[row][col] = 0

        for dr, dc in directions:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] > 0:
                matrix[nr][nc] -= bomb

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]>0:
            alive+=1
            sum+=matrix[i][j]
        

print(f"Alive cells: {alive}")
print(f"Sum: {sum}")

for row in matrix:
    print(*row)