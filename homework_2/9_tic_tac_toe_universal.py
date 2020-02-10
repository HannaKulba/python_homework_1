def determine_winner(char, game_matrix):
    length = len(game_matrix[0])
    width = len(game_matrix)
    winner_count = width
    diagonals_number = 2  # default value
    if width > length:
        winner_count = length
        diagonals_number = (width - length + 1) * 2
    else:
        diagonals_number = (length - width + 1) * 2

    # check if winner is on horizontal line
    if check_winner_by_line(winner_count, char, game_matrix) == char:
        return char
    # check if winner is on vertical line
    rotated_game_matrix = rotate_matrix(game_matrix)
    if check_winner_by_line(winner_count, char, rotated_game_matrix) == char:
        return char

    counter = winner_count
    if width < diagonals_number // 2 or length < diagonals_number // 2:
        counter = diagonals_number // 2

    counts = []  # for diagonals
    for _ in range(diagonals_number * 2):
        counts.append('')
    return check_winner_by_diagonal(counts, counter, winner_count, char, game_matrix)


def check_winner_by_diagonal(counts, count, winner_count, char, game_matrix):
    # check if winner is by diagonal (from left to right corner)
    for index in range(count):
        for index_1 in range(index, count + index):
            counts[index] += game_matrix[index_1][index]

    # check if winner is by diagonal (from right to left corner)
    for index in reversed(range(count)):
        for index_1 in range(count - index - 1, count * 2 - index - 1):
            counts[count * 2 - index - 1] += game_matrix[index_1][index]

    rotated_counts = rotate_matrix(counts)
    for diagonal in rotated_counts:
        check_winner_str = char * winner_count
        diagonal_str = ''
        for elem in diagonal:
            diagonal_str += elem
        if check_winner_str in diagonal_str:
            return char


def check_winner_by_line(winner_count, char, game_matrix):
    length = len(game_matrix)
    check_strings = []
    for i in range(length):
        check_strings.append('')

    for index in range(length):
        for element in game_matrix[index]:
            check_strings[index] += element
        check_winner_str = char * winner_count
        if check_winner_str in check_strings[index]:
            return char


def rotate_matrix(game_matrix):
    return [[game_matrix[j][i] for j in range(len(game_matrix))] for i in range(len(game_matrix[0]) - 1, -1, -1)]


def is_winner(gamer, mark, game_matrix):
    if 0 <= gamer[0] < len(game_matrix[0]) and 0 <= gamer[1] < len(game_matrix):
        if game_matrix[gamer[0]][gamer[1]] == '.':
            game_matrix[gamer[0]][gamer[1]] = mark
            draw_current_game(game_matrix)
            return determine_winner(mark, game_matrix)
        else:
            print('Error! This field is not empty!')
    else:
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
