"""
Name: Kiersten DeCamp
lab9.py
"""


def build_board():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_list


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    game = board[position - 1]
    if not position == game:
        return True
    else:
        return False


def fill_spot(board:list, position:int, shape:str):
    board[position - 1] = shape.strip().lower()


def winning_game(board: list):
    win_1 = board[0] == board[1] == board[2]
    win_2 = board[3] == board[4] == board[5]
    win_3 = board[6] == board[7] == board[8]
    win_4 = board[0] == board[3] == board[6]
    win_5 = board[1] == board[4] == board[7]
    win_6 = board[2] == board[5] == board[8]
    win_7 = board[0] == board[4] == board[8]
    win_8 = board[2] == board[4] == board[6]
    if win_1:
        return True
    elif win_2:
        return True
    elif win_3:
        return True
    elif win_4:
        return True
    elif win_5:
        return True
    elif win_6:
        return True
    elif win_7:
        return True
    elif win_8:
        return True
    else:
        return False


def game_over(board: list):
    if winning_game(board):
        return True
    for i in board:
        end = str(i)
        if end.isnumeric():
            return False
    return True


def get_winner(board: list):
    win_1 = board[0] == board[1] == board[2]
    win_2 = board[3] == board[4] == board[5]
    win_3 = board[6] == board[7] == board[8]
    win_4 = board[0] == board[3] == board[6]
    win_5 = board[1] == board[4] == board[7]
    win_6 = board[2] == board[5] == board[8]
    win_7 = board[0] == board[4] == board[8]
    win_8 = board[2] == board[4] == board[6]
    if win_1:
        return board[0]
    elif win_2:
        return board[3]
    elif win_3:
        return board[6]
    elif win_4:
        return board[0]
    elif win_5:
        return board[1]
    elif win_6:
        return board[2]
    elif win_7:
        return board[0]
    elif win_8:
        return board[2]
    else:
        return None


def play(board):
    while play(board):
        play_1 = 0
        play_2 = 1

        while not game_over(board):
            if play_1 % 2 == 0:
                play_1 = play_1 + 2
                shape = 'x'
                pos = eval(input("x's, choose a position: "))
            fill_spot(board, pos, shape)
            is_legal(board, pos)
            winning_game(board)
            game_over(board)
            get_winner(board)
    replay = input("play again? ").lower()
    if replay == "y":
        print_board(board)
        build_board()
        position = 0
        fill_spot(board, position, shape)
        is_legal(board, position)
        winning_game(board)
        game_over(board)
        get_winner(board)
        play(board)


def main():
    pass


if __name__ == '__main__':
    main()
