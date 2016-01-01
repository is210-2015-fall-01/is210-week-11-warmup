#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a new class"""


import time


class Snapshot(object):
    """An object that stores Snapshot data.
    """

    def __init__(self):
        """Constructor for the Snapshot class.

        Attribute:
            created: A string.

        Examples:
            >>> mysnap=Snapshot()
            >>> hasattr(mysnap, 'created')
            True
        """
        self.created = time.time()
