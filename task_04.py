#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A task based on subclassing"""


import car


class CustomCar(car.Car):
    """A class that stores CustomCar data, and imports from car module."""

    def __init__(self, color='red', tires=None):
        """A constructor for CustomCar() class.

        Args:
            tires: An argument with a default value of None
            color: An argument with a default value of red
        Attributes:
            color: A string denoting car color
            tires: An argument
            with a default value of None
        """
        self.color = color
        if tires is None:
            self.tires = []
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
            self.tires.append(CustomTire())
        else:
            self.tires = tires
            car.Car.__init__(self, color)


class CustomTire(car.Tire):
    """A class that stores CustomTire data."""
    __maximum_miles = 500
