# usr/bin/env python
# -*- coding: utf-8 -*-
"""Task _04"""

import car


class CustomCar(car.Car):
    """CustomCar inherits from car.Car."""

    def __init__(self, color='orange', tires=None):
        """Explains the args and attributes.

        Args:
            Color: defaults to 'orange'
            tires: defaults to None

        Attributes:
            tires: defaults to None
        """
        car.Car.__init__(self, color)
        self.tires = tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(CustomTire())


class CustomTire(car.Tire):
    """ CustomTire inherits from car.Tire.

    Attributes:
           __maximum_miles: has a value of 500
    """
    __maximum_miles = 500
