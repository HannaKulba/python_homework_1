################################################
# написать игру крестики нолики,
# игроки поочередно вводят координаты в консоль
################################################


matrix = [['', '', ''], ['', '', ''], ['', '', '']]


def determine_winner(ch):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    global matrix

    for arr in matrix:
        if arr.count(ch) == 3:
            return ch
        if arr[0] == ch:
            count_0 += 1
        if arr[1] == ch:
            count_1 += 1
        if arr[2] == ch:
            count_2 += 1

    if count_0 == 3 or count_1 == 3 or count_2 == 3:
        return ch
    elif matrix[0][0] == ch and matrix[1][1] == ch and matrix[2][2] == ch:
        return ch
    elif matrix[0][2] == ch and matrix[1][1] == ch and matrix[2][0] == ch:
        return ch
    else:
        return ''


def add_X_or_O(gamer, mark):
    global matrix
    if 0 <= gamer[0] <= 2 and 0 <= gamer[1] <= 2:
        if matrix[gamer[0]][gamer[1]] == '':
            matrix[gamer[0]][gamer[1]] = mark
            return determine_winner(mark)
        else:
            print('ERROR! This field is not empty!')
    else:
        print('IndexError! Out of matrix bounds')


if __name__ == '__main__':
    c = 0
    result = ''
    while result == '':
        c += 2

        gamer_1 = [int(i) for i in input('gamer 1: ').split()]
        if add_X_or_O(gamer_1, 'X') == 'X':
            result = 'X'
            break

        gamer_2 = [int(i) for i in input('gamer 2: ').split()]
        if add_X_or_O(gamer_2, 'O') == 'O':
            result = 'O'
            break

        if c >= 8:
            result = 'D'
            break
    print(result)
