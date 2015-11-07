# usr/bin/env python
# -*- coding: utf-8 -*-
"""Task _02"""

import time


class Snapshot(object):
    """Explaining the Snapshot Class.

    attributes:
         none
    """
    def __init__(self):
        """ A constructor.

        Args:
            none

        Attributes:
            created(int): A unix timestamp.
        """
        self.created = time.time()
