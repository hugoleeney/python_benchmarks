#!/usr/bin/env python3
"""
Written to work with standard python 3.5.5 (no additional libraries required).

# Purpose

Explores ways to create lists and effects of function calls in loops.


# Instructions

You can simply run this file as a script.


# Summary Conclusion

List comprehensions are fast.


# Sample Output

timing: while loop
runtime=5.308549880981445

timing: range loop
runtime=2.9473440647125244

timing: list comprehension on range
runtime=1.8769159317016602

timing: list comprehension on range with added function call
runtime=1.698132038116455

timing: generator function
runtime=4.114220857620239

timing: generator
runtime=2.9092459678649902

timing: range loop with added function call
runtime=4.195919036865234

timing: list of same elements
runtime=0.2564101219177246

"""

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


num_elements = 10000000


def function_call(i):
    return i


def generator_function():
    for i in range(num_elements):
        yield i


if __name__ == "__main__":

    with timer('while loop'):
        i = 0
        returned = []
        while i < num_elements:
            returned.append(i)
            i += 1

    with timer('range loop'):
        returned = []
        for i in range(num_elements):
            returned.append(i)

    with timer('list comprehension on range'):
        returned = [i for i in range(num_elements)]

    with timer('list comprehension on range with added function call'):
        returned = [i for i in function_call(range(num_elements))]

    with timer('generator function'):
        returned = []
        for i in generator_function():
            returned.append(i)

    with timer('generator'):
        g = (i for i in range(num_elements))
        returned = [i for i in g]

    with timer('range loop with added function call'):
        returned = []
        for i in range(num_elements):
            returned.append(function_call(i))

    with timer('list of same elements'):
        returned = [1]*num_elements

