################################################################################
# функция получает в качестве параметра список со вложенными списками,
# в качестве результата она должна вернуть лист со всеми вложенными элементами
# in [[1, 2, [3, 4]], [5, 6], 7]
# out [1, 2, 3, 4, 5, 6, 7]
################################################################################

def get_list(matrix, result_list=None):
    if result_list is None:
        result_list = []
    for element in matrix:
        if type(element) is list:
            for elem in element:
                if type(elem) is list:
                    get_list(elem, result_list)
                else:
                    result_list.append(elem)
        else:
            result_list.append(element)
    return result_list


if __name__ == '__main__':
    print(get_list([[1, 2, [3, 4]], [5, 6], 7]))
