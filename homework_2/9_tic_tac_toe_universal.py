import numpy as np


def determine_winner(char, game_matrix):
    length = len(game_matrix[0])
    width = len(game_matrix)
    winner_count = width
    if width > length:
        winner_count = length

    rotated_game_matrix = rotate_matrix(game_matrix)
    horizontal_res = check_winner_by_line(winner_count, char, game_matrix)
    vertical_res = check_winner_by_line(winner_count, char, rotated_game_matrix)
    diagonals_res = check_winner_by_diagonal(winner_count, char, game_matrix)

    if horizontal_res == char or vertical_res == char or diagonals_res == char:
        return char


def check_winner_by_diagonal(winner_count, char, game_matrix):
    length = len(game_matrix[0])
    width = len(game_matrix)
    check_winner_str = char * winner_count

    matrix = np.array(game_matrix)
    diagonals = [matrix[::-1, :].diagonal(i) for i in range(-length + 1, width)]
    diagonals.extend(matrix.diagonal(i) for i in range(width - 1, -length, -1))

    for diagonal in diagonals:
        if len(diagonal) == winner_count:
            diagonal_str = ''
            for elem in diagonal:
                diagonal_str += elem
            if check_winner_str == diagonal_str:
                return char


def check_winner_by_line(winner_count, char, game_matrix):
    length = len(game_matrix)
    check_winner_str = char * winner_count

    check_strings = []
    for i in range(length):
        check_strings.append('')

    for index in range(length):
        for element in game_matrix[index]:
            check_strings[index] += element
        if check_winner_str in check_strings[index]:
            return char


def rotate_matrix(game_matrix):
    return [[game_matrix[j][i] for j in range(len(game_matrix))] for i in range(len(game_matrix[0]) - 1, -1, -1)]


def is_winner(gamer, mark, game_matrix):
    if 0 <= gamer[0] < len(game_matrix) and 0 <= gamer[1] < len(game_matrix[0]):
        if game_matrix[gamer[0]][gamer[1]] == '.':
            game_matrix[gamer[0]][gamer[1]] = mark
            draw_current_game(game_matrix)
            return determine_winner(mark, game_matrix)
        else:
            print('Error! This field is not empty!')
    else:
        print('IndexError! List index out of range.')


def draw_current_game(game_matrix):
    for array in game_matrix:
        for element in array:
            print(element, end=' ')
        print()


def create_empty_matrix(length, width):
    if length < 3 or width < 3:
        print('Error! Min length or width must be 3 or more.')
    else:
        game_matrix = [['.' for _ in range(length)] for _ in range(width)]
        draw_current_game(game_matrix)
        return game_matrix


def gamer_move(gamer_num, char, game_matrix):
    gamer = [int(i) for i in input('gamer ' + str(gamer_num) + ': ').split()]
    if is_winner(gamer, char, game_matrix):
        return char
    else:
        return ''


def play_and_print_winner(gamer_1_mark, gamer_2_mark, game_matrix):
    draw = len(game_matrix) * len(game_matrix[0]) - 2
    draw_count = 0
    game_count = 0
    result = ''
    while result == '':
        game_count += 1
        draw_count += 2
        print('Game #' + str(game_count))

        result = gamer_move(1, gamer_1_mark, game_matrix)
        if result == gamer_1_mark:
            break

        result = gamer_move(2, gamer_2_mark, game_matrix)
        if result == gamer_2_mark:
            break

        if draw_count >= draw:
            result = 'D'
            break
    print(result)


if __name__ == '__main__':
    game_matrix_size = [int(i) for i in input('Enter game field size (number columns and rows): ').split()]
    gamer_1_mark = input('Gamer #1 will play with (X or O): ')
    gamer_2_mark = input('Gamer #2 will play with: ')
    matrix = create_empty_matrix(game_matrix_size[0], game_matrix_size[1])
    play_and_print_winner(gamer_1_mark, gamer_2_mark, matrix)
