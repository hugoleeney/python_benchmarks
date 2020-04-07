#!/usr/bin/env python3
"""
python version: 3.5.5
additional libraries: numpy, simplejson
"""


from trials.get_trials_import import get_trial_import_inc
from timer import timer


with timer("1. generator import 1000000 using import generator"):
    for idx, t in enumerate(get_trial_import_inc(1000000, 100)):
        a = t[0]
print()