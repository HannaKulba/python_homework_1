class Element:

    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(dict['name'], dict['symbol'], dict['number'])
