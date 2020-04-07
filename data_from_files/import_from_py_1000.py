#!/usr/bin/env python3

"""
python version: 3.5.5
additional libraries: numpy, simplejson

"""


from timer import timer


with timer("2. import 1000000 x 1000 with static import"):
    from trials.t_1000000.trials import trials
    i = 0
    for t in trials:
        i += 1
print()
print("DONE")
