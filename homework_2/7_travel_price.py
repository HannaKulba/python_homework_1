############################################################################
# написать программу рассчитывающую стоимость поездки
# стоимость состоит из суммы билетов, аренды гостиницы и проката автомобиля
############################################################################

def get_hotel_cost(nights):
    price_one_night = 120
    return nights * price_one_night


def get_ticket_cost(direction):
    if direction == 'Шарлотта':
        return 183
    elif direction == 'Тампа':
        return 220
    elif direction == 'Питтсбург':
        return 222
    elif direction == 'Лос-Анджелес':
        return 475


def get_car_rent_cost(days):
    car_rent_price = 40
    if days >= 7:
        return (car_rent_price * days) - (car_rent_price * days) * 0.1
    elif 3 <= days < 7:
        return (car_rent_price * days) - (car_rent_price * days) * 0.05
    else:
        return car_rent_price * days


def travel_cost(direction, days):
    return get_hotel_cost(days) + get_ticket_cost(direction) + get_car_rent_cost(days)


if __name__ == '__main__':
    print(travel_cost("Шарлотта", 10))
