class Element:

    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number

    def getname(self):
        return self._name

    def getsymbol(self):
        return self._symbol

    def getnumber(self):
        return self._number
