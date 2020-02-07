##############################################################################################
# Отсортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты,
# то есть, сколько раз они появляются в элементах.
# Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке,
# что и первое появление в итерации.
##############################################################################################

def sort_by_count_decrease(list):
    element_max_count = 0
    dict_element_count = {}
    result_list = []

    for element in list:
        count = list.count(element)
        if count > element_max_count:
            element_max_count = count
        dict_element_count.update({element: count})

    sorted_by_decrease_dict = sorted(dict_element_count.items(), key=lambda kv: kv[1], reverse=True)

    for element in sorted_by_decrease_dict:
        # element[1] - quantity of every element in list
        for _ in range(element[1]):
            # element[0] - element of list
            result_list.append(element[0])

    return result_list


if __name__ == '__main__':
    data_list = [7, 8, 6, 5, 4, 7, 7, 8, 9, 0, 8, 7, 4, 4, 4, 0]
    # ['bob', 'bob', 'carl', 'alex', 'bob']
    print(sort_by_count_decrease(data_list))
