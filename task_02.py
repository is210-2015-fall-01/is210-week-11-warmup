#!user/bin/env python
# -*- coding: utf-8 -*-
"""Task 2"""

import time


class Snapshot(object):
    """ A class with time module.
    Args:
        'created': stores time attribute
    Attibutes:
        None
    """

    def __init__(self):
        """ Stores time module.
        Returns:
            Unix Timestamp
        Examples:
            None
        """
        self.created = time.time()
