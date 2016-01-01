#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the docstring for task_03."""


import produce


class Apple(produce.Produce):
    """This is an Apple class.

    Args:
        None.

    Returns:
        None.

    Example:
        >>> print Apple.duration
        5356800
        >>> print produce.Produce.duration
        604800
"""
    duration = 5356800
