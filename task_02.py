#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the docstring for task_02."""


import time


class Snapshot(object):
    """This is the Snapshot class.

    Args:
        None.

    Returns:
        created (int): Unix Epoch Time.

    Example:
        >>> mysnap = Snapshot()
        >>> hasattr(mysnap, 'created')
        True
    """
    def __init__(self):
        self.created = time.time()
