class Bear:
    def __init__(self):
        pass

    def eats(self):
        return 'berries'


class Rabbit:
    def __init__(self):
        pass

    def eats(self):
        return 'clover'


class Octothorpe:
    def __init__(self):
        pass

    def eats(self):
        return 'campers'


bear = Bear()
print(bear.eats())

rabbit = Rabbit()
print(rabbit.eats())

octothorpe = Octothorpe()
print(octothorpe.eats())
