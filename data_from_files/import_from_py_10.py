#!/usr/bin/env python3
"""
python version: 3.5.5
additional libraries: numpy, simplejson

"""


from timer import timer


# 0.05 when compiled
with timer("3. import 1000000 x 1 (or 10)"):
    from trials.t_1000000x1.trials0 import trials
    for t in trials:
        a = t[0]
print()
print("DONE")
