#######################################################################
# функция получает в качестве параметра список со вложенными списками,
# в качестве результата она должна вернуть инверсированный лист
# in [[1, 2, [3, 4]], [5, 6], 7]
# out [7,[6, 5], [4, 3], 2, 1]]
#######################################################################

def get_list(matrix):
    for a in matrix:
        if type(a) is list:
            index = matrix.index(a)
            a = a[::-1]
            matrix[index] = a
            get_list(a)
    return matrix[::-1]


if __name__ == '__main__':
    print(get_list([[1, 7, [3, 66]], [0, [6, 9, 8], 7]]))
