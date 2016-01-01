#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week11 warmup task_2."""

import time


class Snapshot(object):
    """This class will call snapshot and store time."""

    def __init__(self, created=None):
        """This function will call snapshot class.

        Args:
            time:(mix):Time at snapshot.

        Attributes:
            time(mix): Unix timestamp.
        """

        if created is None:
            created = int(time.time())

        self.created = created
