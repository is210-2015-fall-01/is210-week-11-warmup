#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week11 warmup task_03."""


import produce


class Apple(produce.Produce):
    """This class stores the new duration time.

    This module will be subclassing an existing class to slightly alter
    its properties.

    Attributes:
        duration(int): duration of produce

    Example:
        >>> print Apple.duration
        5356800
        >>> print produce.Produce.duration
        604800
    """

    duration = 5356800
