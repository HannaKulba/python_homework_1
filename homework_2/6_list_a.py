################################################################################
# функция получает в качестве параметра список со вложенными списками,
# в качестве результата она должна вернуть лист со всеми вложенными элементами
# in [[1, 2, [3, 4]], [5, 6], 7]
# out [1, 2, 3, 4, 5, 6, 7]
################################################################################

res = []


def get_list(matrix):
    global res
    for a in matrix:
        if type(a) is list:
            for l in a:
                if type(l) is int or type(l) is str or type(l) is bool:
                    res.append(l)
                elif type(l) is list:
                    get_list(l)
        elif type(a) is int or type(a) is str or type(a) is bool:
            res.append(a)
    return res


if __name__ == '__main__':
    print(get_list([7,[6, 5], [4, 3], 2, 1]))
