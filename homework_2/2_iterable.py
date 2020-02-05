##############################################################################################
# Отсортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты,
# то есть, сколько раз они появляются в элементах.
# Если два элемента имеют одинаковую частоту, они должны оказаться в том же порядке,
# что и первое появление в итерации.
##############################################################################################

def sort_by_count_decrease(list):
    max_count = 0
    dict_s_c = {}
    result_list = []

    for a in list:
        count = list.count(a)
        if count > max_count:
            max_count = count
        dict_s_c.update({a: count})

    sorted_by_decrease_dict = sorted(dict_s_c.items(), key=lambda kv: kv[1], reverse=True)

    for i in sorted_by_decrease_dict:
        for j in range(i[1]):
            result_list.append(i[0])

    return result_list


if __name__ == '__main__':
    data_list = [7, 8, 6, 5, 4, 7, 7, 8, 9, 0, 8, 7, 4, 4, 4, 0]
    # ['bob', 'bob', 'carl', 'alex', 'bob']
    print(sort_by_count_decrease(data_list))
