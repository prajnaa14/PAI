#TIC-TAC-TOE
import random

def check_winner(player, board):
   
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    return (all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)))

def next_move(board):
 
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                if check_winner('o', board):
                    return
                board[i][j] = 'x'
                if check_winner('x', board):
                    board[i][j] = 'o'
                    return
                board[i][j] = ' '
    # If no winning move, make a random move
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] == ' ':
            board[row][column] = 'o'
            break

def is_board_full(board):
  
    return all(cell != ' ' for row in board for cell in row)

def display_board(board):
   
    for row in board:
        print(row)

def main():
 
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("You are playing as 'x'")
    while True:
        display_board(board)
        print("Player's Move")
        row = int(input("Enter the row: "))
        column = int(input("Enter the column: "))
        if board[row][column] == ' ':
            board[row][column] = 'x'
            if check_winner('x', board):
                display_board(board)
                print("You Have Won!!")
                break
            elif is_board_full(board):
                display_board(board)
                print("It's a Draw!")
                break
            print("Computer's Move")
            next_move(board)
            if check_winner('o', board):
                display_board(board)
                print("Computer has Won!!")
                break
            elif is_board_full(board):
                display_board(board)
                print("It's a Draw!")
                break
        else:
            print("Enter correct choice")

if __name__ == '__main__':
    main()
    