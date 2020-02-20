class Laser:
    def __init__(self):
        pass

    def does(self):
        return 'disintegrate'


class Claw:
    def __init__(self):
        pass

    def does(self):
        return 'crush'


class SmartPhone:
    def __init__(self):
        pass

    def does(self):
        return 'ring'


class Robot():
    laser = Laser()
    claw = Claw()
    smartphone = SmartPhone()

    def __init__(self):
        pass

    def does(self):
        print(self.laser.does())
        print(self.claw.does())
        print(self.smartphone.does())


robot = Robot()
robot.does()
