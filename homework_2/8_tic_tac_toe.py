################################################
# написать игру крестики нолики,
# игроки поочередно вводят координаты в консоль
################################################


def determine_winner(char, game_matrix):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for array in game_matrix:
        # check if winner is on horizontal line
        if array.count(char) == 3:
            return char
        # check if winner is on vertical line
        if array[0] == char:
            count_0 += 1
        if array[1] == char:
            count_1 += 1
        if array[2] == char:
            count_2 += 1

    if count_0 == 3 or count_1 == 3 or count_2 == 3:
        return char
    elif game_matrix[0][0] == char and game_matrix[1][1] == char and game_matrix[2][2] == char:
        return char
    elif game_matrix[0][2] == char and game_matrix[1][1] == char and game_matrix[2][0] == char:
        return char
    else:
        return ''


def is_winner(gamer, mark, game_matrix):
    if 0 <= gamer[0] <= 2 and 0 <= gamer[1] <= 2:
        if game_matrix[gamer[0]][gamer[1]] == '':
            game_matrix[gamer[0]][gamer[1]] = mark
            return determine_winner(mark, game_matrix)
        else:
            print('ERROR! This field is not empty!')
    else:
        print('IndexError! Out of matrix bounds')


def print_winner():
    game_matrix = [['', '', ''], ['', '', ''], ['', '', '']]
    # the number of moves after which a draw occurs, if no one has won before
    DRAW = 8
    # number of moves during the current game
    count = 0
    result = ''
    while result == '':
        count += 2

        gamer_1 = [int(i) for i in input('gamer 1: ').split()]
        if is_winner(gamer_1, 'X', game_matrix) == 'X':
            result = 'X'
            break

        gamer_2 = [int(i) for i in input('gamer 2: ').split()]
        if is_winner(gamer_2, 'O', game_matrix) == 'O':
            result = 'O'
            break

        if count >= DRAW:
            result = 'D'
            break
    print(result)


if __name__ == '__main__':
    print_winner()
