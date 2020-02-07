############################################################################
# написать программу рассчитывающую стоимость поездки
# стоимость состоит из суммы билетов, аренды гостиницы и проката автомобиля
############################################################################

def get_hotel_cost(nights):
    PRICE_ONE_NIGHT = 120
    return nights * PRICE_ONE_NIGHT


def get_ticket_cost(direction):
    CHARLOTTE_TICKET_PRICE = 183
    TAMPA_TICKET_PRICE = 220
    PITTSBURGH_TICKET_PRICE = 222
    LOS_ANGELES_TICKET_PRICE = 475

    if direction == 'Шарлотта':
        return CHARLOTTE_TICKET_PRICE
    elif direction == 'Тампа':
        return TAMPA_TICKET_PRICE
    elif direction == 'Питтсбург':
        return PITTSBURGH_TICKET_PRICE
    elif direction == 'Лос-Анджелес':
        return LOS_ANGELES_TICKET_PRICE
    else:
        print('Билетов на данное направление нет!')
        return


def get_car_rent_cost(days):
    CAR_RENT_PRICE = 40
    COEFFICIENT_DISCOUNT_7_DAYS_AND_MORE = 0.1
    COEFFICIENT_DISCOUNT_3_7_DAYS = 0.05

    if days >= 7:
        return (CAR_RENT_PRICE * days) - (CAR_RENT_PRICE * days) * COEFFICIENT_DISCOUNT_7_DAYS_AND_MORE
    elif 3 <= days < 7:
        return (CAR_RENT_PRICE * days) - (CAR_RENT_PRICE * days) * COEFFICIENT_DISCOUNT_3_7_DAYS
    else:
        return CAR_RENT_PRICE * days


def travel_cost(direction, days):
    try:
        return get_hotel_cost(days) + get_ticket_cost(direction) + get_car_rent_cost(days)
    except TypeError:
        return None


if __name__ == '__main__':
    direction = input('Укажите направление: ')
    days = int(input('Укажите количество дней: '))
    cost = travel_cost(direction, days)
    if type(cost) is float:
        print('Путешествие в ' + direction + ' на ' + str(days) + ' день/дня/дней стоит ' + str(cost) + '.')
    else:
        print('Невозможно определить стоимость поездки.')
