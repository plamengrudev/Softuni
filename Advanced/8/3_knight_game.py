n=int(input())
board=[[x for x in input()] for _ in range(n)]
knights=[]
removed=0
patterns=[
    (-1,-2),(-2,-1),(-2,1),(-1,2),
    (1,-2),(2,-1),(2,1),(1,2)
]

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j]=="K":
            knights.append([i,j])

while True:
    max_count = 0
    knight_row = 0
    knight_col = 0

    for row in range(n):
        for col in range(n):
            if board[row][col] != "K":
                continue

            count = 0

            for dr, dc in patterns:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == "K":
                    count += 1

            if count > max_count:
                max_count = count
                knight_row = row
                knight_col = col

    if max_count == 0:
        break

    board[knight_row][knight_col] = "0"
    removed += 1

print(removed)
