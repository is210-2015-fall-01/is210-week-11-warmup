#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""wk11 warmup task04"""


import car


class CustomCar(car.Car):
    """ a new version of the car class"""

    def __init__(self, color='blue', tires=None):
        """constructor of CustomCar class

        args:
            tires(int): number of tires used on the car

        attributes:
            None

        return:
            tires(lists): number of tires on the car

        examples:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4

      """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """Tire durability

    Args:
       miles (int): Number of miles on all fours.

    Attributes:
       None
    """

    __maximum_miles = 500
