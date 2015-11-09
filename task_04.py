#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week11 warup task_04."""

import car


class CustomCar(car.Car):
    """This is a parent class.

    Args:
        None.
    """
    def __init__(self, tires=None):
        """This function calls the constructor to do its work

        Args:
            tires(int): car tires.

        Returns:
            returns a list of car tires
        """

        car.Car.__init__(self, tires)
        self.tires = tires
        tires = CustomTire()
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tires)


class CustomTire(car.Tire):
    """This is the class for CustomTire.

    Arg:
        None
    """
    __maximum_miles = 500
