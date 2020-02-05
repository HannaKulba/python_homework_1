###################################################################################
# Крестики и Нолики. Вам дан результат игры, и вы должны решить,
# кто победил или что это ничья.
# Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок.
# В случае ничьи, результат должен быть "D".
###################################################################################
import re


def get_game_results(list):
    results = []

    for string in list:
        l = re.findall('[XO.]', string)
        results.append(l)

    def determine_winner(ch):
        count_0 = 0
        count_1 = 0
        count_2 = 0

        nonlocal results

        for arr in results:
            if arr.count(ch) == 3:
                return True
            if arr[0] == ch:
                count_0 += 1
            if arr[1] == ch:
                count_1 += 1
            if arr[2] == ch:
                count_2 += 1

        if count_0 == 3 or count_1 == 3 or count_2 == 3:
            return True
        elif results[0][0] == ch and results[1][1] == ch and results[2][2] == ch:
            return True
        elif results[0][2] == ch and results[1][1] == ch and results[2][0] == ch:
            return True
        else:
            return False

    return determine_winner


def get_winner(list):
    check_winner = get_game_results(list)

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
