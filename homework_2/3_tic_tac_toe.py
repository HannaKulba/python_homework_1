###################################################################################
# Крестики и Нолики. Вам дан результат игры, и вы должны решить,
# кто победил или что это ничья.
# Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
# В случае ничьи, результат должен быть "D".
###################################################################################
import re

WINNER_DETECTOR_NUMBER = 3


def get_game_results(input_game_results_list):
    game_results_matrix = []

    for string in input_game_results_list:
        results_array = re.findall('[XO.]', string)
        game_results_matrix.append(results_array)

    def is_winner(char):
        nonlocal game_results_matrix
        horizontal_res = check_winner_on_horizontal_line(game_results_matrix, char)
        vertical_res = check_winner_on_vertical_line(game_results_matrix, char)
        diagonals_res = check_winner_by_diagonal(game_results_matrix, char)

        if horizontal_res or vertical_res or diagonals_res:
            return True

    return is_winner


def check_winner_on_horizontal_line(game_matrix, char):
    for results_array in game_matrix:
        if results_array.count(char) == WINNER_DETECTOR_NUMBER:
            return True


def check_winner_on_vertical_line(game_matrix, char):
    def check_column(column_number):
        count = 0
        for results_array in game_matrix:
            if results_array[column_number] == char:
                count += 1

        if count == WINNER_DETECTOR_NUMBER:
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


def get_winner(input_game_results_list):
    check_winner = get_game_results(input_game_results_list)

    if check_winner('X'):
        return 'X'
    elif check_winner('O'):
        return 'O'
    else:
        return 'D'


if __name__ == '__main__':
    print(get_winner([
        "OOX",
        "XXO",
        "OXX"]))
