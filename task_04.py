#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""

import car


class CustomCar(car.Car):
    """My own car"""

    def __init__(self, color='blue', tires=None):
        """Constructor for CustomCar() class.
        Args:
            color (string): Color of the car, defaults to 'blue'.
            tires (list): A list of CustomTire() objects. Defaults to None.
        Attributes:
            car.Car (class): Calls the Car() class.
            tires (list): CustomTire objects to determine miles on Tires.
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """A customized car
    Args:
       miles (int): Number of miles on the Tire.
    Attributes:
        miles (int): Number of miles on the Tire.
    """

    __maximum_miles = 500
