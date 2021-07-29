"""
Classes

Member access / naming
    _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose names start with an underscore.

    single_trailing_underscore_: used by convention to avoid conflicts with Python keyword

    __double_leading_underscore: when naming a class attribute, invokes name mangling (inside class FooBar, __boo becomes _FooBar__boo;

    __double_leading_and_trailing_underscore__: "magic" objects or attributes that live in user-controlled namespaces.
"""


class Vehicle:
    __prevent_mangling = True

    # order is important: named args, var args, keyword args
    def __init__(self, make, model, type_, *args, **kwargs):
        # instance attributes
        self.make = make
        self.model = model
        self.type_ = type_

        self.args = args
        # fake protected attribute
        self._protected = f'{__class__.__name__} use me at your own risk'

        self.options = kwargs

    @classmethod
    def wheels(cls):
        return NotImplementedError

    @staticmethod
    def can_compare(another_class):
        if isinstance(another_class, Vehicle):
            return True
        return False

    def go(self):
        pass

    def stop(self):
        pass


if __name__ == '__main__':
    car = Vehicle('BMW', '1', 'E81', 'asdf', air_contitioning=True, four_wheel_drive=False)
