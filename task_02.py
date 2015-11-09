#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates own class from scratch."""


import time


class Snapshot(object):
    """Snap of Time."""

    def __init__(self):
        """Constructor for Snapshot.
        Args:
            time(mix): the timestamp of unix system.
        Attributes:
            time(mix)
        """
        self.created = time.time()
