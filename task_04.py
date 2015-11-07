#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the docstring for task_04."""


import car


class CustomCar(car.Car):
    """This is a class that has the car.Car class as a parent object.

        This class overwrites the parent class object.

        Args:
            color (str): Default is yellow.
            tires (int): Number of tires. Default is None.

        Attributes:
            Tires (int): Number of tires. Default is None.
"""
    def __init__(self, color='red', tires=None):
        car.Car.__init__(self, color)
        tire_list = []
        if tires is None:
            for _ in range(4):
                tire_list.append(CustomTire())
            self.tires = tire_list
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """This is a class that inherits from car.Tire class.

      Args:
          None.

      Attributes:
          __maximum_miles (int): Default is 500.
"""
    __maximum_miles = 500
