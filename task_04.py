#!user/bin/env python
# -*- coding: utf-8 -*-
"""Task 4"""

import car


class CustomCar(car.Car):
    """ CustomCar class, inherits from Car class"""

    def __init__(self, color='red', tires=None):
        """Overwrites Car method
        Args:
            Color: defaults to 'red'
            tires: defaults to None
        Attributes:
            tires: defaults to None
        """
        car.Car.__init__(self, color)
        if not tires:
            it1, it2, it3 = CustomTire(), CustomTire(), CustomTire()
            it4 = CustomTire()
            self.tires = [it1, it2, it3, it4]
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """Inherits from Tire class
    Attributes:
        __maximum_miles (int): pseudo private, sets maximum miles limit
    """

    __maximum_miles = 500
