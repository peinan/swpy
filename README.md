# swpy: A simple, yet useful stopwatch library for python

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/swpy.svg?logo=python&logoColor=white&style=flat-square)](https://pypi.org/project/swpy/)
[![PyPI](https://img.shields.io/pypi/v/swpy.svg?style=flat-square)](https://pypi.org/project/swpy/)
[![CircleCI](https://img.shields.io/circleci/project/github/peinan/swpy.svg?logo=circleci&style=flat-square)](https://circleci.com/gh/peinan/swpy/tree/master)
[![codecov](https://img.shields.io/codecov/c/gh/peinan/swpy.svg?logo=codecov&style=flat-square)](https://codecov.io/gh/peinan/swpy)
[![PyPI - License](https://img.shields.io/pypi/l/swpy.svg?color=blue&style=flat-square)](https://github.com/peinan/swpy/blob/master/LICENSE)

## Requirements

- Python 3.6+

## Install

Just use pip to install.

```bash
pip install swpy
```

## Usage

### Basic Usage

Import `Timer` class from `swpy`, and use `with` statement to capsule the block where you want timing.

```python
from swpy import Timer
from time import sleep

with Timer():
    sleep(1)
```

Or use `start()` and `stop()` function to controll the timer.

```python
t = Timer()
t.start()
sleep(1)
t.stop()
```

And the output will look like below:

```
[timer-1557406243.3309178] started.
[timer-1557406243.3309178] finish time: 1.00 sec.
```

### Features

#### Name the timer

You can name the timer to make it easy to recognize.

```python
with Timer(name='test timer'):
    sleep(1)
```

Now the timer is renamed to `test timer` !

```
[test timer] started.
[test timer] finish time: 1.00 sec.
```

#### Lap time and Split time

There are two types to measuring time without stoping: lap time and split time. The figure below may help you to understand the differences.

![split_lap_time](https://github.com/peinan/swpy/blob/master/imgs/split_lap_time.png)

We prepared `split` and `lap` functions for this kind of usage. The examples are below.

```python
# measure split time
with Timer('timer') as t:
    sleep(1)
    t.split()
    sleep(1)
    t.split()
    sleep(1)
    t.split()
```

```
# outptus
[timer] started.
[timer] split time:  1.00 sec.
[timer] split time:  2.01 sec.
[timer] split time:  3.01 sec.
[timer] finish time: 3.01 sec.
```

```python
# measure lap time
with Timer('timer') as t:
    sleep(1)
    t.lap()
    sleep(1)
    t.lap()
    sleep(1)
    t.lap()
```

```
# outputs
[timer] started.
[timer] lap time:    1.00 sec.
[timer] lap time:    1.01 sec.
[timer] lap time:    1.00 sec.
[timer] finish time: 3.01 sec.
```

And you can name your lap/split time in the case of measuring several tasks in a single run as below.

```python
with Timer('task timer') as t:
    task1()
    t.lap('task1')
    task2()
    t.lap('task2')
```

```
# outputs
[task timer] started.
[task timer] [task1] lap time:    3.69 sec.
[task timer] [task2] lap time:    4.21 sec.
[task timer] finish time: 7.91 sec.
```

#### Use your own logger

You can use your own logger instead of the default `print`.

```python
from logzero import logger
import logging

with Timer(name='test timer', logger=logger, level=logging.DEBUG):
    sleep(1)
```

It will output using logger.

```
[D 190510 14:41:59 swpy:15] [test timer] started.
[D 190510 14:42:00 swpy:15] [test timer] finish time: 1.01 sec.
```

#### Define your own callback

Sometimes, we want to do something after the job has done like notifying the result to slack, executing the next process and so on. Callback feature will help you to do those.

```python
# define a slack notification function
import requests, json
def send_slack(msg):
    requests.post(SLACK_URL, json.dumps({'text': msg}))

# just specify the callback argument
with Timer(name='experiment-1', callback=send_slack):
    sleep(1)
```

## License

[MIT](https://github.com/peinan/swpy/blob/master/LICENSE)
