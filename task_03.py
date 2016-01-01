#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 11 Task 03 Warmup."""


import produce


class Apple(produce.Produce):
    """Subclass of produce.
    Attributes:
        duration (int): Expiration.
    """

    duration = 5356800

print Apple.duration
print produce.Produce.duration
