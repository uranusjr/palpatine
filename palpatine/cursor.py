#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .utils import out


def move(x, y):
    """Move the cursor the absolute position (x, y) on screen.
    """
    out(x, y, letter='H')


def reset():
    """Move the cursor to the top-left position on screen.
    """
    move(1, 1)


def up(y=1, bol=False):
    """Move the cursor up y lines.

    If ``bol`` is set to ``True``, the cursor will be put to the beginning of
    line. Otherwise it will maintain its current x position.
    """
    letter = 'F' if bol else 'A'
    out(y, letter=letter)


def down(y=1, bol=False):
    """Move the cursor down y lines.

    If ``bol`` is set to ``True``, the cursor will be put to the beginning of
    line. Otherwise it will maintain its current x position.
    """
    letter = 'E' if bol else 'B'
    out(y, letter=letter)


def right(x=1):
    """Move the cursor x columns to the right.
    """
    out(x, letter='C')


def left(x=1):
    """Move the cursor x columns to the left.
    """
    out(x, letter='D')


def vert(value):
    """Convinience function to move the cursor vertically.

    If ``value`` is positive, the cursor will be moved down; negative values
    move the cursor up. If ``value`` is ``0``, this is a no-op.
    """
    if value == 0:
        return
    elif value < 0:
        up(0 - value)
    else:
        down(value)


def hori(value, rel=True):
    """Convinience function to move the cursor horizontally.

    If ``value`` is positive, the cursor will be moved to the right; negative
    values move the cursor to the left. If ``value`` is ``0``, this is a no-op.
    If ``rel`` is set to ``False``, this function moves the cursor to the
    absolute x position of the current line.
    """
    if not rel:
        out(value, letter='G')
        return
    elif value == 0:
        return
    elif value < 0:
        left(0 - value)
    else:
        right(value)


def hide():
    """Hide the cursor from screen.

    The cursor is still available, just not drawn.

    :seealso: :py:func:`show`, :py:func:`set_visible`
    """
    set_visible(False)


def show():
    """Show the cursor from screen.

    :seealso: :py:func:`hide`, :py:func:`set_visible`
    """
    set_visible(True)


def set_visible(visible):
    """Set the cursor’s visibility on screen.

    The cursor is always available, even if it is not visible.

    :seealso: :py:func:`show`, :py:func:`hide`
    """
    letter = 'h' if visible else 'l'
    out('?25', letter=letter)
