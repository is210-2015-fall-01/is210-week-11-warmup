#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""docstring for task 04"""


import car


class CustomCar(car.Car):
    """Subclass from Car."""

    def __init__(self, color='black', tires=None):
        """Constructor for the Car class.

        Args:
            color (string): Color of the car.  Default set to black.
            tires: A list of CustomTire() objects. Defaults set to None.

        Attributes:
            color (string): The color of the car.
            tires (list): A list of tire objects.
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """Custom Car.
    Args:
        miles (int): Number of miles on tires.
    """

    __maximum_miles = 500
