#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import time


class Snapshot(object):
    """A class snapshot.
    Attributes:
        created and assign it the output of time.time()
        which returns the current Unix Timestamp
    """
    def __init__(self):
        self.created = time.time()
