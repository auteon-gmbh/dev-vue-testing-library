"""
Inheritance

MRO Method Resolution Order
    Left to Right Depth first
"""


class Drivable:
    @staticmethod
    def can_drive():
        return True

    def drive(self):
        # some implementation
        pass


class Flyable:
    @staticmethod
    def can_fly():
        return True

    def fly(self):
        # some implementation
        pass


class Vehicle:
    def __init__(self, make, model, type_, *args, **kwargs):
        self.make = make
        self.model = model
        self.type_ = type_
        self._protected = f'{__class__.__name__} use me at your own risk'
        self.__not_inherited = f'{__class__.__name__} you can\'t get me'

        self.options = kwargs

    @classmethod
    def wheels(cls):
        return cls.wheels


class Car(Vehicle, Drivable):
    wheels = 4

    def __init__(self, make, model, type_):
        super().__init__(make, model, type_)


class Motorcycle(Vehicle, Drivable):
    wheels = 2

    def __init__(self, make, model, type_):
        super().__init__(make, model, type_)
        self._wheels_on_ground = self.wheels

    def wheelie(self):
        # look cool
        self._wheels_on_ground = 1


class Plane(Vehicle, Drivable, Flyable):
    wheels = 2

    def __init__(self, make, model, type_):
        super().__init__(make, model, type_)


# is will return True if two vars have the same address in memory
# == the variables are equavalent.
#
# if __name__ == '__main__':
#     vehicle = Vehicle('BMW', '1', 'E81')
#     car = Car('BMW', '1', 'E81')
#     moto = Motorcycle('Ducati', 'Panigale', 'V4')
#     plane = Plane('Airbus', 'A320', 'neo')
