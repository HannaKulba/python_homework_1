############################################################################
# написать программу рассчитывающую стоимость поездки
# стоимость состоит из суммы билетов, аренды гостиницы и проката автомобиля
############################################################################

def get_hotel_cost(nights):
    price_one_night = 120
    return nights * price_one_night


def get_ticket_cost(direction):
    price_directions = {'Шарлотта': 183, 'Тампа': 220, 'Питтсбург': 222, 'Лос-Анджелес': 475}
    try:
        return price_directions[direction]
    except KeyError:
        print('Билетов на данное направление нет!')


def get_car_rent_cost(days):
    car_rent_price = 40
    coefficient_discount_7_days_and_more = 0.1
    coefficient_discount_3_7_days = 0.05

    if days >= 7:
        return (car_rent_price * days) - (car_rent_price * days) * coefficient_discount_7_days_and_more
    elif 3 <= days < 7:
        return (car_rent_price * days) - (car_rent_price * days) * coefficient_discount_3_7_days
    else:
        return car_rent_price * days


def travel_cost(direction, days):
    try:
        return get_hotel_cost(days) + get_ticket_cost(direction) + get_car_rent_cost(days)
    except TypeError:
        return None


if __name__ == '__main__':
    direction = input('Укажите направление: ')
    days = int(input('Укажите количество дней: '))
    cost = travel_cost(direction, days)
    if cost is not None:
        print('Путешествие в ' + direction + ' на ' + str(days) + ' день/дня(ей) стоит ' + str(cost) + ' попугаев(я,й).')
    else:
        print('Невозможно определить стоимость поездки.')
