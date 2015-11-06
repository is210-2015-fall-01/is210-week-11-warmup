#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""


import car


class CustomCar(car.Car):
    """A new class subclassed from Car."""

    def __init__(self, color='red', tires=None):
        """Constructor for the Car() class.

        Args:
            color (string): The color of the car. Defaults to ``'red'``.

        Attributes:
           color (string): The color of the car.
           tires (list): A list of tire objects.
        """
        car.Car.__init__(self, color)
        self.tires = tires if tires is not None else [
            CustomTire() for _ in range(4)]


class CustomTire(car.Tire):
    """A new class subclassed from Tire.

    Has a mileage variable as well.

    Attributes:
        __maximum_miles (numeric): the maximum number of miles a tire obtains.
    """
    __maximum_miles = 500
