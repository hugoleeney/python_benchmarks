#!/usr/bin/env python3
"""
Written to work with standard python 3.5.5 (no additional libraries required).

# Purpose

Explores the fastest way to generate a 50/50 random variable.


# Instructions

You can simply run this file as a script.


# Summary Conclusion

Using random.random and comparing to 0.5 is much faster than using random.choice([0,1]).


# Sample Output

timing: use_random
4999421
runtime=2.049018144607544

timing: use_choice
5001631
runtime=16.556126832962036
"""

import random
from time import time


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


def do_test_n_times(n, boolean_test):
    results = 0
    for i in range(n):
        if boolean_test(i):
            results += 1
    return results


n = 10000000


with timer("use_random"):
    print(do_test_n_times(n, lambda x: random.random() < 0.5))


with timer("use_choice"):
    print(do_test_n_times(n, lambda x: random.choice([0,1])))
