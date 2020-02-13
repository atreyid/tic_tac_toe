import random

def display_board(board):
    print('\n'*100)
    row = []
    for i in range(1, 10):
        row.append(board[i])
        if i % 3 == 0:
            print(' | '.join(row))
            row = []




def player_input(player: int) -> (str, str):
    marker =''
    while marker != 'X' and marker != 'O':
        marker = input('Player {}: Choose marker X or O '.format(player + 1))
        # marker = input('Player 1: Choose marker X or O ')
    # if marker == 'X':
    #     return ('X', 'O')
    # return ('O', 'X')
    if player == 0:
        if marker == 'X':
            return (marker, 'O')
        else:
            return (marker, 'X')
    else:
        if marker == 'X':
            return ('O', marker)
        else:
            return ('X', marker)



def player_choice(board):
    next_move=int(input("Enter move between 1-9: "))
    if space_check(board, next_move):
        return next_move
    else:
        print("Position occupied...")
        return player_choice(board)


    
def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    status=False
    if board[1]==board[2]==board[3]==mark:
        status=True
    elif board[4]==board[5]==board[6]==mark: 
        status = True
    elif board[7]==board[8]==board[9]==mark:
        status = True
    elif board[1]==board[4]==board[7]==mark:
        status = True
    elif board[2]==board[5]==board[8]==mark:
        status = True
    elif board[3]==board[6]==board[9]==mark:
        status = True
    elif board[1]==board[5]==board[9]==mark:
        status = True
    elif board[3]==board[5]==board[7]==mark:
        status = True
    return status

def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False


def full_board(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def choose_first():
    return random.randint(0,1)

def replay():
    choice=input("Do you want to continue playing? Enter Y or N ")
    if choice == 'Y':
        return True
    else:
        return False



#Putting together of the code starts here

print('Welcome to Tic Tac Toe!')
while True:
    board = [' ' for i in range(10)]
    board[0] = '#'
    choice = choose_first()

    print("Player {} will go first".format(choice + 1))

    if choice == 0:
        first_player = 0
        second_player = 1
    else:
        first_player = 1
        second_player = 0

    markers = player_input(first_player)
    # markers = player_input()

    # print("Player {} will go first".format(choice + 1))

    game_on = True
    # break
    while game_on:
        position = player_choice(board)
        place_marker(board, markers[first_player], position)
        display_board(board)
        won = win_check(board,markers[0])
        if won:
            print("Player 1 won!")
            break
        won = win_check(board,markers[1])
        if won:
            print("Player 2 won!")
            break

        if not full_board(board):
            position = player_choice(board)
            place_marker(board, markers[second_player], position)
            display_board(board)
            won = win_check(board,markers[0])
            if won:
                print("Player 1 won!")
                break
            won = win_check(board,markers[1])
            if won:
                print("Player 2 won!")
                break
        else:
            print("Game tied")
            break

    if not replay():
        break
    else:
        continue
#Done !