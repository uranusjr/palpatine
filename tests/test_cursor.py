#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import nose
from nose.tools import eq_

import palpatine

from .utils import _patch_stdout


def setup():
    palpatine.init()


def teardown():
    palpatine.deinit()


class MoveTests(unittest.TestCase):

    @_patch_stdout
    def test_standard(self, stdout):
        palpatine.cursor.move(x=4, y=5)
        eq_(stdout.getvalue(), '\x1b[4;5H')


class UpTests(unittest.TestCase):

    @_patch_stdout
    def test_default(self, stdout):
        palpatine.cursor.up()
        eq_(stdout.getvalue(), '\x1b[1A')

    @_patch_stdout
    def test_bol(self, stdout):
        palpatine.cursor.up(bol=True)
        eq_(stdout.getvalue(), '\x1b[1F')

    @_patch_stdout
    def test_y(self, stdout):
        palpatine.cursor.up(y=4)
        eq_(stdout.getvalue(), '\x1b[4A')

    @_patch_stdout
    def test_standard(self, stdout):
        palpatine.cursor.up(y=4, bol=True)
        eq_(stdout.getvalue(), '\x1b[4F')


class DownTests(unittest.TestCase):

    @_patch_stdout
    def test_default(self, stdout):
        palpatine.cursor.down()
        eq_(stdout.getvalue(), '\x1b[1B')

    @_patch_stdout
    def test_bol(self, stdout):
        palpatine.cursor.down(bol=True)
        eq_(stdout.getvalue(), '\x1b[1E')

    @_patch_stdout
    def test_y(self, stdout):
        palpatine.cursor.down(y=4)
        eq_(stdout.getvalue(), '\x1b[4B')

    @_patch_stdout
    def test_standard(self, stdout):
        palpatine.cursor.down(y=4, bol=True)
        eq_(stdout.getvalue(), '\x1b[4E')


class RightTests(unittest.TestCase):

    @_patch_stdout
    def test_default(self, stdout):
        palpatine.cursor.right()
        eq_(stdout.getvalue(), '\x1b[1C')

    @_patch_stdout
    def test_standard(self, stdout):
        palpatine.cursor.right(x=5)
        eq_(stdout.getvalue(), '\x1b[5C')


class LeftTests(unittest.TestCase):

    @_patch_stdout
    def test_default(self, stdout):
        palpatine.cursor.left()
        eq_(stdout.getvalue(), '\x1b[1D')

    @_patch_stdout
    def test_standard(self, stdout):
        palpatine.cursor.left(x=5)
        eq_(stdout.getvalue(), '\x1b[5D')


# TODO: Complete tests.


if __name__ == '__main__':
    nose.main()
