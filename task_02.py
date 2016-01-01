#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A snapshot in time."""


import time


class Snapshot(object):
    """Timely calculations.

    Returns the cuurent time.

    Args:
        None

    Attributes:
        created (numeric): Assigns the current timestamp.
    """

    def __init__(self):
        self.created = time.time()
