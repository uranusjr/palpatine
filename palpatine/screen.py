#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import const
from .utils import out


def clear(clear_type=const.ALL):
    """Clear a part, or all of the screen.

    The cursor is *not* moved after the screen is cleared. You will need to call
    cursor-moving functions (see :py:mod:`.cursor`) to move it manually.

    :param clear_type: What part of the screen should be cleared. See
        :py:mod:`.const` for a list of possible choices.
    """
    out(clear_type, letter='J')


def scroll(value):
    """Scroll the screen.

    Scroll the screen by ``value`` lines. If ``value`` is positive, the screen
    if scrolled down; negative values scroll the screen up. If ``value`` is
    ``0``, this is a no-op.
    """
    if value == 0:
        return
    elif value < 0:
        out(0 - value, letter='S')
    else:
        out(value, letter='T')
