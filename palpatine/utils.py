#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import os

__all__ = ['init', 'deinit', 'out']


def _call_colorama(func_name, silent=True):
    try:
        import colorama
    except ImportError:
        # POSIX systems do not really require colorama (only Windows does),
        # so if we're on one of those we can just pretend this worked.
        if os.name != 'posix':
            raise
    else:
        getattr(colorama, func_name)()


def init():
    """Initialize Palpatine.

    Call this at the start of your program to initialize Palpatine. Some
    monkey-patching will happen on certain systems (e.g. Windows) to make
    Palpatine work.

    :seealso: :py:func:`deinit`.
    """
    _call_colorama('init')


def deinit():
    """De-initialization Palpatine.

    Call this to disable Palpatine. This does not always disable Palpatine
    completely, but only restores some monkey-patched elements. Use it only
    if you run into problems with those monkey-patched things.

    :seealso: :py:func:`init`, :py:func:`reinit`.
    """
    _call_colorama('deinit')


def reinit():
    """Re-Initialize Palpatine after de-initialized it.

    Call this to re-initialize Palpatine after you call :py:func:`deinit`. This
    is similar with :py:func:`init`, but is a tad cheaper to call if you are
    certain that you already called :py:func:`init` previously.

    :seealso: :py:func:`init`, :py:func:`deinit`.
    """
    _call_colorama('reinit')


def out(*params, **options):
    """Outputs a ASCII escape command to console.

    Palpatine works by sending ASCII escape sequences to your terminal. If you
    want to send your own sequences, maybe to achieve some advanced operations
    not covered by Palpatine, this is the function for you.

    :seealso: https://en.wikipedia.org/wiki/ANSI_escape_code
    """
    csi = options.get('csi', '\x1b')
    letter = options.get('letter', '')
    code = '{csi}[{n}{letter}'.format(
        csi=csi,
        n=';'.join((str(i) for i in params)),
        letter=letter,
    )
    print(code, end='')
