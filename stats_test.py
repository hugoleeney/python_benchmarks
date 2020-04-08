#!/usr/bin/env python3
"""
Written to work with standard python 3.5.5 (external libraries required: numpy==1.18.2).


# Purpose

Explores the fastest way to run simple statistics on arrays of numbers.


# Instructions

If you have numpy installed then you can just run this as a script.


# Summary Conclusion

For non-trivial cases it is quicker to create a numpy array and use numpy functions. 
You can run numpy functions on python lists but it would seem you have the same overhead of converting to numpy array.
There is no advantage gained when running numpy functions more than once.


# Sample Output

timing: create array
runtime=4.32141900062561

timing: copy array
runtime=0.016638994216918945

timing: create numpy array
runtime=0.09427499771118164

timing: python min
python_min=0
runtime=0.025493144989013672

timing: statistics mean
statistics_mean=49951.713239
runtime=1.287816047668457

timing: statistics stddev
statistics_stdev=28862.75487516741
runtime=5.2155139446258545

timing: numpy min on python
numpy_min=0
runtime=0.10659909248352051

timing: numpy mean on python
49951.713239
runtime=0.1568741798400879

timing: numpy stddev on python
28862.740443786366
runtime=0.12770605087280273

timing: numpy min
numpy_min=0
runtime=0.002084016799926758

timing: numpy mean
49951.713239
runtime=0.001786947250366211

timing: numpy stddev
28862.740443786366
runtime=0.010833978652954102
"""


import random
import statistics
from time import time

import math
import numpy as np

class timer:
    def __init__(self, name="timer"):
        self.name = name
    def __enter__(self):
        print("timing: %s"%self.name)
        self.starttime = time()
    def __exit__(self, type, value, traceback):
        endtime = time()
        self.total_time = endtime-self.starttime
        print("runtime=%s"%(self.total_time))
        print()


with timer("create array"):
    a = []
    for i in range(1000000):
        a.append(random.randint(0,100000))

with timer("copy array"):
    python_a = list(a)

with timer("create numpy array"):
    numpy_a = np.array(python_a)

with timer("python min"):
    python_min = min(python_a)
    print("python_min=%s"%python_min)

with timer("statistics mean"):
    statistics_mean = statistics.mean(python_a)
    print("statistics_mean=%s"%statistics_mean)

with timer("statistics stddev"):
    statistics_stdev = statistics.stdev(python_a)
    print("statistics_stdev=%s"%statistics_stdev)


with timer("numpy min on python"):
    numpy_min = np.min(python_a)
    print("numpy_min=%s"%numpy_min)

with timer("numpy mean on python"):
    numpy_mean = np.mean(python_a)
    print(numpy_mean)

with timer("numpy stddev on python"):
    numpy_stddev = np.std(python_a)
    print(numpy_stddev)


numpy_a = np.array(python_a)

with timer("numpy min"):
    numpy_min = np.min(numpy_a)
    print("numpy_min=%s"%numpy_min)

numpy_a = np.array(python_a)

with timer("numpy mean"):
    numpy_mean = np.mean(numpy_a)
    print(numpy_mean)

numpy_a = np.array(python_a)

with timer("numpy stddev"):
    numpy_stddev = np.std(numpy_a)
    print(numpy_stddev)

with timer("numpy stddev again on same array"):
    numpy_stddev = np.std(numpy_a)
    print(numpy_stddev)


assert math.isclose(statistics_mean, numpy_mean, abs_tol=1), "%s %s"%(statistics_mean, numpy_mean)

assert math.isclose(statistics_stdev, numpy_stddev, abs_tol=1), "%s %s"%(statistics_stdev, numpy_stddev)

