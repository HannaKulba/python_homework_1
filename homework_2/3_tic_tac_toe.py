###################################################################################
# Крестики и Нолики. Вам дан результат игры, и вы должны решить,
# кто победил или что это ничья.
# Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
# В случае ничьи, результат должен быть "D".
###################################################################################
import re


def get_game_results(input_game_results_list):
    game_results_matrix = []

    for string in input_game_results_list:
        results_array = re.findall('[XO.]', string)
        game_results_matrix.append(results_array)

    def determine_winner(character):
        count_0 = 0
        count_1 = 0
        count_2 = 0

        nonlocal game_results_matrix

        for results_array in game_results_matrix:
            # check if winner is on horizontal line
            if results_array.count(character) == 3:
                return True
            # check if winner is on vertical line
            if results_array[0] == character:
                count_0 += 1
            if results_array[1] == character:
                count_1 += 1
            if results_array[2] == character:
                count_2 += 1

        if count_0 == 3 or count_1 == 3 or count_2 == 3:
            return True
        elif game_results_matrix[0][0] == character and game_results_matrix[1][1] == character and \
                game_results_matrix[2][2] == character:
            return True
        elif game_results_matrix[0][2] == character and game_results_matrix[1][1] == character and \
                game_results_matrix[2][0] == character:
            return True
        else:
            return False

    return determine_winner


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
