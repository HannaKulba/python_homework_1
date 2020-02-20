class Element:

    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    # def dump(self):
    #     print(self.name)
    #     print(self.symbol)
    #     print(self.number)

    def __str__(self):
        print(self.name)
        print(self.symbol)
        print(self.number)


# def dump
# hydrogen = Element('Hydrogen', 'H', 1)
# print(hydrogen)  # <__main__.Element object at 0x00000234E6C461F0>

# def __str__
hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)  # Hydrogen \n H \n 1 \n TypeError: __str__ returned non-string (type NoneType)
