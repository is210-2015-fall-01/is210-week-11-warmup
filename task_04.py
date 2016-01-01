#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Uses subclassing to show has-a and is-a concepts."""


import car


class CustomCar(car.Car):
    """New car class. Sub"""

    def __init__(self, color='blue', tires=None):
        """A custom car constructor.
        Args:
            color(str): color of car
            tires(list): list of object, default to None
        Attributes:
            tires(list)
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """CustomTire constructor.
    Args:
        miles(int): number of miles
    """
    __maximum_miles = 500
