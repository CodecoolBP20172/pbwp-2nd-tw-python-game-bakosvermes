import os


def draw_board(board):
    print()
    print('     TIC TAC TOE')
    print()
    print()
    print('       |     |')
    print('    ' + board[7] + '  | ' + board[8] + '   | ' + board[9])
    print('       |     |')
    print('  -----------------')
    print('       |     |')
    print('    ' + board[4] + '  | ' + board[5] + '   | ' + board[6])
    print('       |     |')
    print('  -----------------')
    print('       |     |')
    print('    ' + board[1] + '  | ' + board[2] + '   | ' + board[3])
    print('       |     |')


def player_input(player):
    while True:
        try:
            user_input = int(input('Press 1 to select Player1 or press 2 for Player2 '))
        except ValueError:
            continue
        if user_input not in range(1, 3):
            continue
            player = user_input
        return player


def set_letter(player):
    if player == 1:
        letter = 'x'
    else:
        player == 2
        letter = 'o'
    return letter


def illegal_move(board, move):
    return board[move] != ' '


def player_move(board, letter):
    print("miki")
    move = ' '
    while move not in list(range(1, 10)) or illegal_move(board, move):
        print('Select an empty space between 1 and 9')
        try:
            move = int(input())
        except ValueError:
            continue
    board[move] = letter
    return board


def check_wins(board, letter):
    return ((board[7] == board[8] and board[8] == board[9] and board[9] == letter) or
            (board[4] == board[5] and board[5] == board[6] and board[6] == letter) or
            (board[1] == board[2] and board[2] == board[3] and board[3] == letter) or
            (board[7] == board[4] and board[4] == board[1] and board[1] == letter) or
            (board[9] == board[6] and board[6] == board[3] and board[3] == letter) or
            (board[7] == board[5] and board[5] == board[3] and board[3] == letter) or
            (board[8] == board[5] and board[5] == board[2] and board[2] == letter) or
            (board[0] == board[5] and board[5] == board[1] and board[1] == letter))


def check_tie(board):
    tie = 0
    for i in board[1:10]:
        for j in i:
            if j != ' ':
                tie += 1
    return tie


def status(board, letter):
    if check_wins(board, letter):
        print('win')
        game_is_on = False
    elif check_tie(board) == 9:
        print('tie')
        game_is_on = False


def turn(player):
    player = 1
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    return player


def main():
    try:
        while True:
            os.system('clear')
            board = [' '] * 10
            # score
            draw_board(board)
            player = 1
            player_input(player)
            letter = set_letter(player)
            game_is_on = True
            while game_is_on:
                turn(player)
                print(player)
                player_move(board, letter)
                os.system('clear')
                draw_board(board)
                check_wins(board, letter)
                check_tie(board)
                status(board, letter)
                turn(player)
                print(player)
                set_letter(player)

    except KeyboardInterrupt:
        print('\n' 'See you next time')
    return board

main()