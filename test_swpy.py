#!/usr/bin/env python
# coding: utf-8
#
# Filename:   test_swpy.py
# Author:     Peinan ZHANG
# Created at: 2019-05-09

from swpy import Timer

import time

import unittest
from unittest.mock import Mock


class TimerTestCase(unittest.TestCase):

    def test_time_elapsed(self):
        with Timer() as t:
            time.sleep(1)

        self.assertAlmostEqual(t.elapsed, 1, 1)

    def test_callback(self):
        true_msg = '[test] finish time: 0.50 sec.'
        f = Mock()

        with Timer(name='test', callback=f):
            time.sleep(0.5)

        f.assert_called_once_with(true_msg)

    def test_start(self):
        true_msg = '[test] finish time: 0.50 sec.'
        f = Mock()

        t = Timer(name='test', callback=f)
        time.sleep(0.1)
        t.start()
        time.sleep(0.5)
        t.stop()

        self.assertAlmostEqual(t.elapsed, 0.5, 1)
        f.assert_called_once_with(true_msg)

    def test_stop(self):
        true_msg = '[test] finish time: 0.50 sec.'
        f = Mock()

        t = Timer(name='test')
        time.sleep(0.5)
        t.stop(callback=f)

        self.assertAlmostEqual(t.elapsed, 0.5, 1)
        f.assert_called_once_with(true_msg)

    def test_split(self):
        true_msg = '[test] split time:  0.50 sec.'
        f = Mock()

        t = Timer(name='test')
        time.sleep(0.2)
        t.split()
        time.sleep(0.3)
        t.split(callback=f)
        time.sleep(0.1)
        t.stop()

        self.assertAlmostEqual(t.elapsed, 0.6, 1)
        f.assert_called_once_with(true_msg)

    def test_lap(self):
        true_msg = '[test] lap time:    0.20 sec.'
        f = Mock()

        t = Timer(name='test')
        time.sleep(0.3)
        t.lap()
        time.sleep(0.2)
        t.lap(callback=f)
        time.sleep(0.1)
        t.stop()

        self.assertAlmostEqual(t.elapsed, 0.6, 1)
        f.assert_called_once_with(true_msg)

