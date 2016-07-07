#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module defines the exceptions of MASS.
"""


class TaskWait(Exception):
    """Raised to notify that the task is in progress.
    """
    pass


class TaskError(Exception):

    """Raised while task error.
    """

    def __init__(self, reason, details=None):
        super(TaskError, self).__init__()
        self.reason = reason
        self.details = details


class UnsupportedScheduler(Exception):
    """Raised while scheduler is not supported.
    """
    pass
