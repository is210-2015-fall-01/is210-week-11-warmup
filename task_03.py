#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module subclasses an existing class to alter its properties."""


import produce


class Apple(produce.Produce):
    """A constructor for Apple duration.
    Args:
        Produce(object): duration of produce
    Attribute:
        duration(int): duration of produce
    """

    duration = 5356800
