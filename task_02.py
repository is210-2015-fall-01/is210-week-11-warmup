#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docatring for task 02"""


import time


class Snapshot(object):
    """calculates time.

    Returns current time.

    Args:
        None.

    Attributes:
        created (numeric): Assignment of current time.
    """

    def __init__(self):
        self.created = time.time()
