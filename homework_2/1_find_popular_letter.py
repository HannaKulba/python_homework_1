###########################################################################################################
# Дан текст, который содержит различные английские буквы и знаки препинания. 
# Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". 
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, 
# которая идет первой в алфавите.
###########################################################################################################

import re


def find_popular_letter(input_string):
    input_string = re.findall('[a-z]', input_string.lower())
    dict_letter_count = {}
    letter_max_count = input_string.count(input_string[0])
    popular_letter = ''

    for letter in input_string:
        count = input_string.count(letter)
        if count >= letter_max_count:
            letter_max_count = count
            dict_letter_count.update({letter: count})
            popular_letter = letter

    for letter in dict_letter_count.keys():
        if dict_letter_count[letter] == letter_max_count:
            if ord(popular_letter) > ord(letter):
                popular_letter = letter

    return popular_letter


if __name__ == '__main__':
    string = input()
    print(find_popular_letter(string))
