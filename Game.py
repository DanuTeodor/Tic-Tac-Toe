import random
import time

game_board = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9'],
]

# to see if the board is full
def board_full(game_board):
    '''
    It will return False if in game baord is at least one '_'
    It will return True if in game board full with 'X' and 'O'
    '''
    num = ['1','2','3','4','5','6','7','8','9']
    for a in game_board:
        for a1 in a:
            for n in num:
                if a1 == n:
                    return False
    return True

# to verify if a move is valid on table
def verif_move(move, game_board):
    '''

    :param move: to know where you will put the 'X' and 'O'
    to put X and O the only one thing to verify is that in matrix is '_' and no 'X' or 'O'
    :param game_board: to see in the whole game board
    :return: True if it is a valid move
    '''
    if move == 1:
        if game_board[0][0] == '1':
            return True
    elif move == 2:
        if game_board[0][1] == '2':
            return True
    elif move == 3:
        if game_board[0][2] == '3':
            return True
    elif move == 4:
        if game_board[1][0] == '4':
            return True
    elif move == 5:
        if game_board[1][1] == '5':
            return True
    elif move == 6:
        if game_board[1][2] == '6':
            return True
    elif move == 7:
        if game_board[2][0] == '7':
            return True
    elif move == 8:
        if game_board[2][1] == '8':
            return True
    elif move == 9:
        if game_board[2][2] == '9':
            return True
    return False

# to put the move on the board
def put_move(move, player):
    '''
    :param move: the place where will be the 'X' or the 'O'
    and move = 1 is the first element in matrix, move = 2 is the second element in matrix and so
    :param player: to know what to put in matrix
    '''
    if player == 1:
        if move == 1:
            game_board[0][0] = 'X'
        elif move == 2:
            game_board[0][1] = 'X'
        elif move == 3:
            game_board[0][2] = 'X'
        elif move == 4:
            game_board[1][0] = 'X'
        elif move == 5:
            game_board[1][1] = 'X'
        elif move == 6:
            game_board[1][2] = 'X'
        elif move == 7:
            game_board[2][0] = 'X'
        elif move == 8:
            game_board[2][1] = 'X'
        elif move == 9:
            game_board[2][2] = 'X'
    elif player == -1:
        if move == 1:
            game_board[0][0] = 'O'
        elif move == 2:
            game_board[0][1] = 'O'
        elif move == 3:
            game_board[0][2] = 'O'
        elif move == 4:
            game_board[1][0] = 'O'
        elif move == 5:
            game_board[1][1] = 'O'
        elif move == 6:
            game_board[1][2] = 'O'
        elif move == 7:
            game_board[2][0] = 'O'
        elif move == 8:
            game_board[2][1] = 'O'
        elif move == 9:
            game_board[2][2] = 'O'

# to se if the game it's over
def game_finsh(game_board):
    # check the condition to win
    for i in range(3):
        # horizontally
        if game_board[0][0] == game_board[0][1] and game_board[0][1] == game_board[0][2]:
            return True
        if game_board[1][0] == game_board[1][1] and game_board[1][1] == game_board[1][2]:
            return True
        if game_board[2][0] == game_board[2][1] and game_board[2][1] == game_board[2][2]:
            return True

        # vertically
        if game_board[0][0] == game_board[1][0] and game_board[1][0] == game_board[2][0]:
            return True
        if game_board[0][1] == game_board[1][1] and game_board[1][1] == game_board[2][1]:
            return True
        if game_board[0][2] == game_board[1][2] and game_board[1][2] == game_board[2][2]:
            return True

        # diagonally
        if game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]:
            return True
        if game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]:
            return True
    return False

# to print the board
def print_board(game_board):
    for i in range(3):
        print (game_board[i])

# search if it have 1 move to win
def condition_win(col, row):
    # search if it have 2 on the same row
    if game_board[col-2][row] == game_board [col-1][row]:
        return True
    #searcj if it have 2 on the same col
    if game_board[col][row-2] == game_board [col][row-1]:
        return True

    # search if it have 2 on pricipal diagonal
    if col == row:
        if (game_board[1][1] == game_board[2][2]) or (game_board[2][2] == game_board[3][3]) or (game_board[1][1] == game_board[3][3]):
            return True
    # search if it have 2 on secundar diagonal
    if game_board[0][2] == game_board[1][1] or game_board[1][1] == game_board[2][0] or game_board[0][2] == game_board[2][0]:
        return True
    return False

# search if it have 1 move to lose
def condition_lose(col, row):
    # search if it have 2 on the same row
    if game_board[col - 2][row] == game_board[col - 1][row]:
        return True
    # searcj if it have 2 on the same col
    if game_board[col][row - 2] == game_board[col][row - 1]:
        return True

    # search if it have 2 on pricipal diagonal
    if col == row:
        if game_board[1][1] == game_board[2][2] or game_board[2][2] == game_board[3][3] or game_board[1][1] == game_board[3][3]:
            return True
    # search if it have 2 on secundar diagonal
    if game_board[0][2] == game_board[1][1] or game_board[1][1] == game_board[2][0] or game_board[0][2] == game_board[2][0]:
        return True
    return False

# search for a move
def searching():
    for col in range(3):
        for row in range(3):
            if ('X' in game_board[col-1][row]) or ('X' in game_board[col-2][row]):
                game_board[col][row] = 'X'
            elif ('X' in game_board[col][row-1]) or ('X' in game_board[col][row-2]):
                game_board[col][row] = 'X'
            elif ('X' in game_board[1][1]) or ('X' in game_board[0][0]) or ('X' in game_board[2][2]):
                game_board[col][row] = 'X'
            elif ('X' in game_board[0][2]) or ('X' in game_board[1][1]) or ('X' in game_board[2][0]):
                game_board[col][row] = 'X'
            else:
                random_moves()
# medium AI
def analysis_board():
    something = True
    something2 = True
    for col in range(3):
        for row in range(3):
            if condition_lose(col, row) == True:
                game_board[col][row] = 'O'
                something2 = False
            if condition_win(col, row) == True:
                game_board[col][row] = 'O'
                something = False
    if something == True and something2 == True:
        searching()




# Easy AI with random moves
def random_moves():
    # generate a random nomber between 1 and 9
    random_variable = random.randint(1,9)
    # check of it's valid
    if verif_move(random_variable, game_board) == True:
        put_move(random_variable, -1)
    # if not try again
    elif verif_move(random_variable, game_board) == False:
        while verif_move(random_variable, game_board) == False:
            random_variable = random.randint(1,9)
        put_move(random_variable, -1)

# the AI
def computer_move(difficulty):
    # the easiest difficulty
    if difficulty == 0:
        random_moves()
    # the medium difficulty
    elif difficulty == 1:
        # had the change at least 55% to make a minimax move and 45% to do a random move
        chance = random.uniform(0,1) <= 55 / 100.0
        if chance >= 55:
            analysis_board()
        else:
            random_moves()

print("If you want to play agaist another player press 1. If you want to play agaist computer press 0")
player_vs_player = int(input())
# player vs player0
if(player_vs_player == 1):
    print("Please put numbers between 1 and 9")
    print("Player1 is X and Player2 have O")
    print("Good luck for both of you!")
    player1 = 1
    finish = False
    print_board(game_board)

    while finish == False:
        if player1 == 1: # player1 turn
            print("Player1's turn")
            x = int(input("Where do you want to move?"))
            # check the move
            if verif_move(x, game_board) == True:
                put_move(x, player1) # put the move it's valid
                print_board(game_board)
            # try again if it's not valid
            elif verif_move(x, game_board) == False or x > 9 or x < 1:
                while verif_move(x, game_board) == False:
                    print("Invalid move. Please put again")
                    x = int(input("Where do you want to move?"))
                    if verif_move(x, game_board) == True:
                        put_move(x, player1)
                        print_board(game_board)
            player1 =  -1
        else: # player2 turn
            print("Player2's turn")
            x = int(input("Where do you want to move?"))
            #check the move
            if verif_move(x, game_board) == True:
                put_move(x, player1) # put the move if it's valid
                print_board(game_board)
            # try again if it's not valid
            elif verif_move(x, game_board) == False or x > 9 or x < 1:
                while verif_move(x, game_board) == False:
                    print("Invalid move. Please put again")
                    x = int(input("Where do you want to move?"))
                    if verif_move(x, game_board) == True:
                        put_move(x, player1)
                        print_board(game_board)
            player1 = 1
        #to see if game it's over
        if game_finsh(game_board) == True:
            if player1 == -1:
                print("Player1 has won")
                finish = True
            if player1 == 1:
                print("Player2 has won")
                finish = True
        if game_finsh(game_board) == False and board_full(game_board) == True:
            print("It's tie")
            finish = True
else: # player vs computer
    print("Select the difficulty for computer")
    print("0 - for easy, 1 - medium")
    difficulty = int(input())
    print("You are with 'X' and the computer is with 'O'. Good luck!")
    print_board(game_board)
    player1 = 1
    while game_finsh(game_board) == False:
        if player1 == 1: # this is for player
            print("Player's turn ")
            x = int(input("Where do you want to move?"))
            # check if the move is valid
            if verif_move(x, game_board) == True:
                put_move(x, player1) # put the move in board if it's valid
                print_board(game_board)
            # if the move is not valid will try again
            elif verif_move(x, game_board) == False or x > 9 or x < 1:
                while verif_move(x, game_board) == False:
                    print("Invalid move. Please put again")
                    x = int(input("Where do you want to move?"))
                    if verif_move(x, game_board) == True:
                        put_move(x, player1)
                        print_board(game_board)
            player1 = -1
            time.sleep(1)
        else: # this is the computer move
            print("Computer's turn")
            computer_move(difficulty)
            print_board(game_board)
            player1 = 1

        #see if the game it's over
        if game_finsh(game_board) == True:
            if player1 == 1:
                print("Computer has won!")
            elif player1 == -1:
                print("Player has won!")
        if (game_finsh(game_board) == False) and (board_full(game_board) == True):
            print("It's tie!")
            finish = True
