################################################
# написать игру крестики нолики (3х3),
# игроки поочередно вводят координаты в консоль
################################################

MATRIX_SIZE = 3


def check_winner_on_horizontal_line(game_matrix, char):
    for results_array in game_matrix:
        if results_array.count(char) == MATRIX_SIZE:
            return True


def check_winner_on_vertical_line(game_matrix, char):
    def check_column(column_number):
        count = 0
        for results_array in game_matrix:
            if results_array[column_number] == char:
                count += 1

        if count == MATRIX_SIZE:
            return True

    if check_column(0) or check_column(1) or check_column(2):
        return True


def check_winner_by_diagonal(game_matrix, char):
    def diagonal(cell_1, cell_2, cell_3):
        if game_matrix[cell_1[0]][cell_1[1]] == char and game_matrix[cell_2[0]][cell_2[1]] == char and \
                game_matrix[cell_3[0]][cell_3[1]] == char:
            return True

    if diagonal((0, 0), (1, 1), (2, 2)) or diagonal((0, 2), (1, 1), (2, 0)):
        return True


def get_winner(char, game_matrix):
    horizontal_res = check_winner_on_horizontal_line(game_matrix, char)
    vertical_res = check_winner_on_vertical_line(game_matrix, char)
    diagonals_res = check_winner_by_diagonal(game_matrix, char)

    if horizontal_res or vertical_res or diagonals_res:
        return True


def is_winner(gamer, mark, game_matrix):
    if 0 <= gamer[0] <= 2 and 0 <= gamer[1] <= 2:
        if game_matrix[gamer[0]][gamer[1]] == '':
            game_matrix[gamer[0]][gamer[1]] = mark
            return get_winner(mark, game_matrix)
        else:
            print('ERROR! This field is not empty!')
    else:
        print('IndexError! Out of matrix bounds')


def gamer_move(gamer_num, char, game_matrix):
    gamer = [int(i) for i in input('gamer ' + str(gamer_num) + ': ').split()]
    if is_winner(gamer, char, game_matrix):
        return char
    else:
        return ''


def play_and_print_winner(gamer_1_mark, gamer_2_mark):
    game_matrix = [['' for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]  # create empty matrix
    draw = 8  # the number of moves after which a draw occurs, if no one has won before
    count = 0  # number of moves during the current game
    result = ''
    while result == '':
        count += 2

        result = gamer_move(1, gamer_1_mark, game_matrix)  # gamer_1
        if result == gamer_1_mark:
            break

        result = gamer_move(2, gamer_2_mark, game_matrix)  # gamer_2
        if result == gamer_2_mark:
            break

        if count >= draw:
            result = 'D'
            break
    print(result)


if __name__ == '__main__':
    gamer_1_mark = input('Gamer #1 will play with (X or O): ')
    gamer_2_mark = input('Gamer #2 will play with: ')
    play_and_print_winner(gamer_1_mark, gamer_2_mark)
