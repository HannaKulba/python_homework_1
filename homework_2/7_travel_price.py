############################################################################
# написать программу рассчитывающую стоимость поездки
# стоимость состоит из суммы билетов, аренды гостиницы и проката автомобиля
############################################################################

def get_hotel_cost(nights):
    price_one_night = 120
    return nights * price_one_night


def get_ticket_cost(direction):
    prices = {'Шарлотта': 183, 'Тампа': 220, 'Питтсбург': 222, 'Лос-Анджелес': 475}
    try:
        return prices[direction]
    except KeyError:
        print('Билетов на данное направление нет!')


def get_car_rent_cost(days):
    def calculate_car_rent_cost(price, days, coefficient=0.0):
        return (price * days) - (price * days) * coefficient

    car_rent_price = 40
    coefficient_discount_7_days_and_more = 0.1
    coefficient_discount_3_7_days = 0.05

    if days >= 7:
        return calculate_car_rent_cost(car_rent_price, days, coefficient_discount_7_days_and_more)
    elif 3 <= days < 7:
        return calculate_car_rent_cost(car_rent_price, days, coefficient_discount_3_7_days)
    else:
        return calculate_car_rent_cost(car_rent_price, days)


def travel_cost(direction, days):
    try:
        return get_hotel_cost(days) + get_ticket_cost(direction) + get_car_rent_cost(days)
    except TypeError:
        return None


def print_cost(cost, direction, days):
    if cost is not None:
        print(
            'Путешествие в ' + direction + ' на ' + str(days) + ' день/дня(ей) стоит ' + str(cost) + ' попугаев(я,й).')
    else:
        print('Невозможно определить стоимость поездки.')


if __name__ == '__main__':
    direction = input('Укажите направление: ')
    days = int(input('Укажите количество дней: '))
    cost = travel_cost(direction, days)
    print_cost(cost, direction, days)
