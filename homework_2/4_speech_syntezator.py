#################################################################################
# Речевой модуль Стефана сломался. Этот модуль отвечал за произношение чисел. 
# Для него сейчас большая проблема произносить составные числа. 
# Помогите нашему Роботу заговорить правильно и освоить хотя бы первую тысячу. 
# Стефан должен говорить на английском, так что вам нужно знать 
# правила составления чисел в английском языке. 
# Все слова в строковом представлении числа должны быть разделены одним пробелом. 
# Будьте осторожны с пробелами -- очень сложно увидеть двойной пробел, 
# но это критично для компьютера.
#################################################################################


def synthesize_speech(number):
    if number <= 10:
        return numbers_till_10(number)
    elif 10 < number < 20:
        return numbers_from_11_till_19(number)
    elif 20 <= number < 100:
        return numbers_from_20_till_90(number)
    elif 100 <= number <= 1000:
        return numbers_from_100_till_1000(number)


def numbers_till_10(number):
    if number == 0:
        return ''
    elif number == 1:
        return 'one'
    elif number == 2:
        return 'two'
    elif number == 3:
        return 'three'
    elif number == 4:
        return 'four'
    elif number == 5:
        return 'five'
    elif number == 6:
        return 'six'
    elif number == 7:
        return 'seven'
    elif number == 8:
        return 'eight'
    elif number == 9:
        return 'nine'
    elif number == 10:
        return 'ten'


def numbers_from_11_till_19(number):
    if number == 11:
        return 'eleven'
    elif number == 12:
        return 'twelve'
    elif number == 13:
        return 'thirteen'
    elif number == 15:
        return 'fifteen'
    elif number == 18:
        return 'eighteen'
    elif number in [14, 16, 17, 19]:
        return numbers_till_10(number % 10) + 'teen'


def numbers_from_20_till_90(number):
    if 20 <= number < 30:
        return 'twenty' + ' ' + numbers_till_10(number % 10)
    elif 30 <= number < 40:
        return 'thirty' + ' ' + numbers_till_10(number % 10)
    elif 40 <= number < 50:
        return 'forty' + ' ' + numbers_till_10(number % 10)
    elif 50 <= number < 60:
        return 'fifty' + ' ' + numbers_till_10(number % 10)
    elif 80 <= number < 90:
        return 'eighty' + ' ' + numbers_till_10(number % 10)
    elif 60 <= number < 80 or 90 <= number < 100:
        return numbers_till_10(number // 10) + 'ty' + ' ' + numbers_till_10(number % 10)


def numbers_from_100_till_1000(number):
    if number % 1000 == 0:
        return numbers_till_10(number // 1000) + ' thousand'
    else:
        hundreds = number // 100
        tens = number % 100
        result = numbers_till_10(hundreds) + ' hundred '
        if tens <= 10:
            result += numbers_till_10(tens)
        elif 10 < tens < 20:
            result += numbers_from_11_till_19(tens)
        elif 20 <= tens < 100:
            result += numbers_from_20_till_90(tens)
        return result


if __name__ == '__main__':
    input_number = int(input())
    print(synthesize_speech(input_number))
