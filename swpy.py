#!/usr/bin/env python
# coding: utf-8
#
# Filename:   swpy.py
# Author:     Peinan ZHANG
# Created at: 2019-05-09

import time
import logging


class Timer:
    def __init__(self, name=None, logger=None, level=logging.DEBUG, digits=2, callback=None):
        self.name = name if name else f'timer-{time.time()}'
        self.print = print if not logger else lambda msg: logger.log(level, msg)
        self.level = level
        self.digits = digits
        self.callback = callback

        self.started_at = time.time()
        self.times = [self.started_at]
        self.print(f'[{self.name}] started.')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stopped_at = time.time()
        self.times.append(self.stopped_at)

        self.elapsed = self.stopped_at - self.started_at

        msg = f'[{self.name}] finish time: {self.elapsed:.{self.digits}f} sec.'
        self.print(msg)

        if self.callback: self.callback(msg)

    def start(self, callback=None):
        self.started_at = time.time()
        self.times[0] = self.started_at

        msg = f'[{self.name}] started.'
        self.print(msg)

        if callback: callback(msg)

    def stop(self, callback=None):
        self.stopped_at = time.time()
        self.times.append(self.stopped_at)

        self.elapsed = self.stopped_at - self.started_at

        msg = f'[{self.name}] finish time: {self.elapsed:.{self.digits}f} sec.'
        self.print(msg)

        if callback: callback(msg)
        elif self.callback: self.callback(msg)

    def split(self, callback=None):
        self.times.append(time.time())
        msg = f'[{self.name}] split time:  {self.times[-1] - self.times[0]:.{self.digits}f} sec.'
        self.print(msg)

        if callback: callback(msg)

    def lap(self, callback=None):
        self.times.append(time.time())
        msg = f'[{self.name}] lap time:    {self.times[-1] - self.times[-2]:.{self.digits}f} sec.'
        self.print(msg)

        if callback: callback(msg)

