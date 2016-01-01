#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Task 02 Warmup."""

import time


class Snapshot(object):
    """Unix timestamp.
    Attributes: None
    """

    def __init__(self):
        """Constructor for Snapshot() class.
        Args:
            time(int): Unix timestamp
        Attributes:
            time(int): Unix timestamp
        """
        self.created = time.time()
