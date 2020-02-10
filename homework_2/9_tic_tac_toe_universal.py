def determine_winner(char, game_matrix):
    winner_count = len(game_matrix)
    if len(game_matrix) > len(game_matrix[0]):
        winner_count = len(game_matrix[0])

    check_strings = []
    for i in range(winner_count):
        check_strings.append('')

    # check if winner is on horizontal line
    for array in game_matrix:
        if array.count(char) == winner_count:
            return char

    # check if winner is on vertical line
    rotated_game_matrix = rotate_matrix(game_matrix)
    for index in range(len(rotated_game_matrix)):
        for element in rotated_game_matrix[index]:
            check_strings[index] += element
        check_winner_str = char * winner_count
        if check_strings[index].__contains__(check_winner_str):
            return char

    counts = []  # four diagonals (diagonal is line that begins in the corner)
    for i in range(4):
        counts.append(0)

    # check if winner is by diagonal
    for index in range(winner_count):
        if game_matrix[index][index] == char:  # 1
            counts[0] += 1
        if game_matrix[index][winner_count - 1 - index] == char:  # 2
            counts[1] += 1
        if game_matrix[index + 1][index] == char:  # 3
            counts[2] += 1
        if game_matrix[index + 1][winner_count - 1 - index] == char:  # 4
            counts[3] += 1

    for count in counts:
        if count == winner_count:
            return char


def rotate_matrix(game_matrix):
    return [[game_matrix[j][i] for j in range(len(game_matrix))] for i in range(len(game_matrix[0]) - 1, -1, -1)]


def is_winner(gamer, mark, game_matrix):
    try:
        if game_matrix[gamer[0]][gamer[1]] == '.':
            game_matrix[gamer[0]][gamer[1]] = mark
            draw_current_game(game_matrix)
            return determine_winner(mark, game_matrix)
        else:
            print('Error! This field is not empty!')
    except IndexError:
        print('IndexError! List index out of range.')


def print_winner(game_matrix):
    X = 'X'  # gamer_1 mark
    O = 'O'  # gamer_2 mark
    DRAW = len(game_matrix) * len(game_matrix[0]) - 2
    count_draw = 0
    count = 0
    result = ''
    while result == '':
        count += 1
        count_draw += 2
        print('Game #' + str(count))
        gamer_1 = [int(i) for i in input('gamer 1: ').split()]
        if is_winner(gamer_1, X, game_matrix) == X:
            result = X
            break

        gamer_2 = [int(i) for i in input('gamer 2: ').split()]
        if is_winner(gamer_2, O, game_matrix) == O:
            result = O
            break

        if count_draw >= DRAW:
            result = 'D'
            break
    print(result)


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


if __name__ == '__main__':
    game_matrix_size = [int(i) for i in input().split()]
    matrix = create_empty_matrix(game_matrix_size[0], game_matrix_size[1])  # columns rows
    print_winner(matrix)
