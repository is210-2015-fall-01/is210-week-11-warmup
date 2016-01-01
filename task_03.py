#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclassing an existing class"""


import produce


class Apple(produce.Produce):
    """An object that stores Apple data, and imports from produce module.

    Attributes:
        duration(int): A long integer.
    """
    duration = 5356800
