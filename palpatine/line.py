#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import const
from .utils import out


def clear(clear_type=const.ALL):
    """Clear part of, or all characters in the current line.

    The cursor is *not* moved after the line is cleared. You will need to call
    cursor-moving functions (see :py:mod:`.cursor`) to move it manually.

    :param clear_type: What part of the current line should be cleared. See
        :py:mod:`.const` for a list of possible choices.
    """
    out(clear_type, letter='K')
