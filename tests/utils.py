#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import StringIO
from mock import patch


_patch_stdout = patch('sys.stdout', new_callable=StringIO)
