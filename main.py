import random

board = ["","","", "", "", "", "", "", ""]
player1_symbol = "O"
player2_symbol = "X"
computer_symbol = "C"

def draw_board(board):
    for i in range(0, 9, 3):
        print(board[i : i + 3])


def check_game_winner(board,player):
    if (
        board[0]
        and board[1]
        and board[2] == player
        or board[3]
        and board[4]
        and board[5] == player
        or board[6]
        and board[7]
        and board[8] == player
        or board[0]
        and board[3]
        and board[6] == player
        or board[1]
        and board[4]
        and board[7] == player
        or board[2]
        and board[5]
        and board[8] == player
        or board[0]
        and board[4]
        and board[8] == player
        or board[2]
        and board[4]
        and board[6] == player
    ):
       return True  
    return False
def computer_fill_board(board):
    position = random.randrange(0,9)
    while (board[position] != ""):
        position = random.randrange(0,9)
         
    board[position] = "C"
    draw_board(board)

def player_fill_board(board,player):
    position = int(input("Please choose a position from 0-8:"))
    
    while (board[position] != ""):
        print(f"Position {position} already occupied please choose a different position")
        position = int(input("Please choose a position from 0-9:"))
         
    board[position] = player
    draw_board(board)

def game_play(board,symbol,symbol2):
    while True:
        if symbol == "C":
            print("Computer playing")
            
            computer_fill_board(board)
            if check_game_winner(board,symbol):
                print("Computer wins")
                break
        if symbol == "X" or symbol2 == "X":    
            print("Player One playing")

            player_fill_board(board,symbol)
            if check_game_winner(board,symbol):
                print("Player One wins")
                break
        else:
            print("Player Two playing")
            player_fill_board(board,symbol2)
            if check_game_winner(board,symbol2):
                print("Player Two wins")
                break
    draw_board(board)

def main():
    game_mode =int(input("Please choose 1 for Computer vs Player or 2 for Player vs Player: "))
    if game_mode == 1:
        game_play(board,computer_symbol,player1_symbol)
    elif game_mode == 2:
        game_play(board,player1_symbol,player2_symbol)
    else:
        print("Please choose the correct option next time")
        
if __name__ == "__main__":
    main()
