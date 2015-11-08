#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 01"""

import produce

TOMATO = produce.Produce()
EGGPLANT = produce.Produce(11311210802)
TOMATO_ARRIVAL = TOMATO.arrival
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
