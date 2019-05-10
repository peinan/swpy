# swpy: A simple, yet useful stopwatch library for python

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/swpy.svg?style=flat-square)](https://pypi.org/project/swpy/)
[![PyPI](https://img.shields.io/pypi/v/swpy.svg?style=flat-square)](https://pypi.org/project/swpy/)
[![CircleCI](https://img.shields.io/circleci/project/github/peinan/swpy.svg?logo=circleci&style=flat-square)](https://circleci.com/gh/peinan/swpy/tree/master)
[![codecov](https://img.shields.io/codecov/c/gh/peinan/swpy.svg?logo=codecov&style=flat-square)](https://codecov.io/gh/peinan/swpy)
[![PyPI - License](https://img.shields.io/pypi/l/swpy.svg?color=blue&style=flat-square)](https://github.com/peinan/swpy/blob/master/LICENSE)

## Requirements

- Python 3.6+

## Install

```bash
$ pip install swpy
```

## Usage

```python
>>> from swpy import Timer
>>> import time


# the simplest use
>>> with Timer():
...   time.sleep(1)

[timer-1557406243.3309178] started.
[timer-1557406243.3309178] finish time: 1.00 sec.


# name the timer for visibility
>>> with Timer(name='test timer'):
...     time.sleep(1)

[test timer] started.
[test timer] finish time: 1.00 sec.


# use your own logger
>>> from logzero import logger
>>> import logging
>>> with Timer(name='test timer', logger=logger, level=logging.DEBUG):
...     time.sleep(1)

[D 190510 14:41:59 swpy:15] [test timer] started.
[D 190510 14:42:00 swpy:15] [test timer] finish time: 1.01 sec.


# process the timer result with your own function with callback
## define a slack notification function
>>> import requests, json
>>> def send_slack(msg):
...     requests.post(SLACK_URL, json.dumps({'text': msg}))

## just specify the callback argument
>>> with Timer(name='experiment-1', logger=logger, level=logging.DEBUG, callback=send_slack):
...     time.sleep(1)
[D 190510 14:48:17 swpy:15] [experiment-1] started.
[D 190510 14:48:18 swpy:15] [experiment-1] finish time: 1.01 sec.
```

## License

MIT
