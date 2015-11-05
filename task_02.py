#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Task 02 Warmup."""

import time


class Snapshot(object):
    """Unix timestamp."""

    def __init__(self):
        """Constructor for Snapshot() class."""
        self.created = time.time()
