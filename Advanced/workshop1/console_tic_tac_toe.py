def print_board(current_board):
    for i in range(len(current_board)):
        print("| {} | {} | {} |".format(*current_board[i]))

def check_status(current_board):
    has_winner=False
    winning_sign=None
    signs=['X','O']
    for sign in signs:
        if not has_winner:
            for i in range(len(current_board)):
                for j in range(len(current_board[i])):
                    if current_board[i][0]==current_board[i][1]==current_board[i][2]==sign:
                        has_winner=True
                        winning_sign=sign
                    elif current_board[0][j]==current_board[1][j]==current_board[2][j]==sign:
                        has_winner=True
                        winning_sign=sign
            if current_board[0][0]==current_board[1][1]==current_board[2][2]==sign:
                has_winner=True
                winning_sign=sign
            elif current_board[0][2]==current_board[1][1]==current_board[2][0]==sign:
                has_winner=True
                winning_sign=sign
    return has_winner,winning_sign


print(f"Player one name: ",end="")
player1=input()
print(f"Player two name: ",end="")
player2=input()
current_player=None
symbol_player1=None
symbol_player2=None
board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print(f"{player1} would you like to play with 'X' or 'O'? ",end="")
symbol_player1=input()
symbol_player2='X' if symbol_player1=='O' else 'O'
print(f"This is the numeration of the board:\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")
print(f"{player1} starts first!")
current_player=player1
current_sign=symbol_player1
winner=None
is_won=False
winning_sign=None
while True:
    print(f"{current_player} choose a free position [1-9]: ",end="")
    position=int(input())-1
    row=position//3
    column=position%3
    board[row][column]=current_sign
    print_board(board)
    is_won,winning_sign=check_status(board)
    if is_won:
        winner=player1 if winning_sign==symbol_player1 else player2
        print(f"{winner} won!")
        break
    else:
        current_player=player1 if current_player==player2 else player2
        current_sign=symbol_player1 if current_sign==symbol_player2 else symbol_player2






