###### Tic-Tac-Toe Game ######
playing = True
# Setting up the board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"


def display_board():
    print(
        f"{board[0]} | {board[1]} | {board[2]}\n" \
        f"---------\n" \
        f"{board[3]} | {board[4]} | {board[5]}\n" \
        f"---------\n" \
        f"{board[6]} | {board[7]} | {board[8]}\n"
    )


# Player Turns
def player_turn():
    print(f"{current_player} player turn!")
    space = input(f"Where would you like to place your {current_player}? (type 1-9): ")
    space = int(space) - 1
    if type(board[space]) is int:
        board[space] = current_player
    else:
        print("That space is already occupied! try another space!\n")
        player_turn()


#def o_player_turn():
#    print("O player turn!")
#    space = input("Where would you like to place your O? (type 1-9): ")
#    space = int(space) - 1
#    if type(board[space]) is int:
#        board[space] = 'O'
#    else:
#        print("That space is already occupied! try another space!\n")
#        o_player_turn()


def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


# Win Conditions
def win_check():
    global playing
    if board[0] == board[1] == board[2]:
        winner = board[0]
        playing = False
        return winner
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        playing = False
        return winner
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        playing = False
        return winner
    elif board[0] == board[4] == board[8]:
        winner = board[0]
        playing = False
        return winner
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        playing = False
        return winner
    elif board[0] == board[3] == board[7]:
        winner = board[0]
        playing = False
        return winner
    elif board[1] == board[4] == board[7]:
        winner = board[0]
        playing = False
        return winner
    elif board[2] == board[5] == board[8]:
        winner = board[0]
        playing = False
        return winner

# Game Start
display_board()
while playing is True:
    player_turn()
    display_board()
    change_player()
    win = win_check()



print(f'{win} Player Wins!')
