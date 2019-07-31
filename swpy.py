"""
swpy
====

A simple, yet useful stopwatch library.

Usage
-----

Use context manager or initializing with class, it depends on you.

Example:
    >>> from swpy import Timer
    >>> import time

    # the way of using context manager
    >>> with Timer():
    ...     time.sleep(1)

    [timer-1557406243.3309178] started.
    [timer-1557406243.3309178] finish time: 1.00 sec.

    # the way of using initializing class
    >>> timer = Timer():
    >>> time.sleep(1)
    >>> timer.stop()

    [timer-1557406243.3309178] started.
    [timer-1557406243.3309178] finish time: 1.00 sec.
"""

import logging
import time

__author__ = 'Peinan ZHANG'
__version__ = (0, 1, 2)
__license__ = 'MIT'


class Timer:
    def __init__(self, name=None, logger=None, level=logging.DEBUG, digits=2, callback=None):
        """
        Args:
            :param name str: The name of the timer. default: 'time-{NOW}'
            :param logger logger: Specific the logger. default: print
            :param level: The log level while using logger.
            :param digits int: The digit of time demical. digits=2 will look like 1.00.
            :param callback callable: The callback.

        Example:
            >>> with Timer():
            ...   time.sleep(1)

            [timer-1557406243.3309178] started.
            [timer-1557406243.3309178] finish time: 1.00 sec.
        """
        self.timername = name if name else f'timer-{time.time()}'
        self.print = print if not logger else lambda msg: logger.log(level, msg)
        self.level = level
        self.digits = digits
        self.callback = callback

        self.started_at = time.time()
        self.times = [self.started_at]
        self.stopped_at = None
        self.elapsed = None
        self.print(f'[{self.timername}] started.')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stopped_at = time.time()
        self.times.append(self.stopped_at)

        self.elapsed = self.stopped_at - self.started_at

        msg = f'[{self.timername}] finish time: {self.elapsed:.{self.digits}f} sec.'
        self.print(msg)

        if self.callback: self.callback(msg)

    def start(self, title='', callback=None):
        self.started_at = time.time()
        self.times[0] = self.started_at

        title_block = f'[{title}] ' if title else ''
        msg = f'[{self.timername}] {title_block}started.'
        self.print(msg)

        if callback: callback(msg)

    def stop(self, title='', callback=None):
        self.stopped_at = time.time()
        self.times.append(self.stopped_at)

        self.elapsed = self.stopped_at - self.started_at

        title_block = f'[{title}] ' if title else ''
        msg = f'[{self.timername}] {title_block}finish time: {self.elapsed:.{self.digits}f} sec.'
        self.print(msg)

        if callback: callback(msg)
        elif self.callback: self.callback(msg)

    def split(self, title='', callback=None):
        self.times.append(time.time())
        title_block = f'[{title}] ' if title else ''
        msg = f'[{self.timername}] {title_block}split time:  {self.times[-1] - self.times[0]:.{self.digits}f} sec.'
        self.print(msg)

        if callback: callback(msg)

    def lap(self, title='', callback=None):
        self.times.append(time.time())
        title_block = f'[{title}] ' if title else ''
        msg = f'[{self.timername}] {title_block}lap time:    {self.times[-1] - self.times[-2]:.{self.digits}f} sec.'
        self.print(msg)

        if callback: callback(msg)

