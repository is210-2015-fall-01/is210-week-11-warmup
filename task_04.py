#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Task 04 Warmup"""


import car


class CustomCar(car.Car):
    """ object that store properties of custom car
    args:
        car.Car: properties of Car
    attributes:
        None
    """

    def __init__(self, tires=None):
        """constructor of CustomCar class
        args:
            tires(int): number of tires
        attributes:
            tires(int): number of tires
        return:
            Number of tires
        exampls:
            >>> mycar = CustomCar()
            >>> len(mycar.tires)
            4
            >>> isinstance(mycar.tires[0], CustomTire)
            True
        """
        car.Car.__init__(self)
        self.tires = tires

        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
               self.tires.append(CustomTire())


class CustomTire(car.Tire):
        """Max Miles
    args:
        car.tire(): car stats
    attributes:
         __maximum_miles(int): max miles default 500
        """
        __maximum_miles = 500
