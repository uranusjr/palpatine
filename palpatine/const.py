#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module defines several constants to use with functions that require
options to use.
"""

AFTER = 0
"""Used with clear functions.

If supplied, the clear function will clear everything *after* the cursor.

:seealso: :py:func:`.screen.clear`, :py:func:`.line.clear`
"""

BEFORE = 1
"""Used with clear functions.

If supplied, the clear function will clear everything *before* the cursor.

:seealso: :py:func:`.screen.clear`, :py:func:`.line.clear`
"""

ALL = 2
"""Used with clear functions.

If supplied, the clear function will clear the entire context (e.g. either the
current line, or the whole screen).

:seealso: :py:func:`.screen.clear`, :py:func:`.line.clear`
"""
