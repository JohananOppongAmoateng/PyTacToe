board = ["","","", "", "", "", "", "", ""]
player1 = "O"
player2 = "X"


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

def fill_board(board,player):
    position = int(input("Please choose a position from 0-8:"))
    
    while (board[position] != ""):
        print(f"Position {position} already occupied please choose a different position")
        position = int(input("Please choose a position from 0-9:"))
         
    board[position] = player
    draw_board(board) 

def main():
    while True:
        print("Player One playing")
        
        fill_board(board,player1)
        if check_game_winner(board,player1):
            print("Player One wins")
            break
        
        print("Player Two playing")
        fill_board(board,player2)
        if check_game_winner(board,player2):
            print("Player Two wins")
            break
        
# if __name__ == "main":
main()
