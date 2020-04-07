#!/usr/bin/env python3
"""
python version: 3.5.5
additional libraries: numpy, simplejson


# Purpose

Explores the fastest way to acquire large sequences of random numbers - in this particular case
each number in the sequence changes by one from the number before. The tests include generating
the sequences from scratch or loading them from a pre-generated file in various formats. The conlusion drawn here
may be applicable to any program that may need to load data from a file or has the option to
generate data from scratch or pre-generate and store data.


# Instructions

To run the test in full you need to generate and precompile a number of files. Run
the following commands from the source directory where this script is kept first (sub-directories
trials from repo should be present)
e.g. python -m gen_trials <output format> <trial size> <num trials per file> <file prefix> <output dir> <num files>
/$ python -m trials.gen_trials py 1000000 10 trials/t_1000000 trials 100
/$ python -m trials.gen_trials py 1000000 1 trials/t_1000000x1 trials 1
/$ python -m trials.gen_trials json_slow 1000000 1 trials/t_1000000x1 trials 1
/$ python -m trials.gen_trials py_split 1000000 10 trials/t_1000000 splittrials 1
/$ python -m trials.gen_trials json_slow 1000000 100 trials/t_1000000x100 trials 2

Then run this script. The first time you run it the tests that use python files will be slow and
generatre pyc files. The second time you run it these tests will run much quicker.


# Summary Conclusion

generating numbers to a python file and compiling that to a pyc file is
a fast approach assuming that you able to compile the pyc files in advance.


# Sample Output (first run)

timing: 1. generator import 1000000 x 1000
runtime=4290.350818872452

timing: 2. import 1000000 x 1000 with static import
runtime=0.09725689888000488

timing: 3. import 1000000 x 1 (or 10)
runtime=1.618945837020874

timing: 4. generator import 1000000 x 1
runtime=0.00015306472778320312

timing: 5. generator import 1000000 x 10
runtime=0.001316070556640625

timing: 6. import 1000000x10 splittrials (10 trials)
runtime=40.90775680541992

timing: 7. generator generate 1000000 x 10
runtime=8.306110143661499
time per trial=0.8306

timing: 8. generate 1000000 x 10
runtime=8.113124132156372
time per trial=0.8113

timing: 9. simplejson 1000000 x 1
runtime=0.12929415702819824

timing: 10. simplejson 1000000 x 100
runtime=30.330846071243286

timing: 11. json 1000000 x 100
runtime=21.835952043533325

timing: 12. read 1000000 x 10 from binary one by one
runtime=13.753793954849243

timing: read 1000000 x 10 from binary as struct
runtime=3.4108150005340576

DONE


# Sample Output (second run)

timing: 1. generator import 1000000 x 1000
runtime=55.85879683494568

timing: 2. import 1000000 x 1000 with static import
runtime=0.003556966781616211

timing: 3. import 1000000 x 1 (or 10)
runtime=0.09471392631530762

timing: 4. generator import 1000000 x 1
runtime=0.00019621849060058594

timing: 5. generator import 1000000 x 10
runtime=0.0004699230194091797

timing: 6. import 1000000x10 splittrials (10 trials)
runtime=0.5248990058898926

timing: 7. generator generate 1000000 x 10
runtime=9.460197925567627
time per trial=0.9460

timing: 8. generate 1000000 x 10
runtime=10.713544845581055
time per trial=1.0714

timing: 9. simplejson 1000000 x 1
runtime=0.2190389633178711

timing: 10. simplejson 1000000 x 100
runtime=56.62112212181091

timing: 11. json 1000000 x 100
runtime=27.42050790786743

DONE

"""


import numpy
import simplejson

import json
import struct

from trials.inc_dec import gen_pos_numbers_inc_dec
from trials.get_trials_import import get_trial_import
from timer import timer


def get_trial(trial_size, num_trials):
    for i in range(num_trials):
        trial = numpy.array(gen_pos_numbers_inc_dec(trial_size, up_chance=0.5))
        yield (min(trial), numpy.mean(trial), numpy.std(trial), trial)

if __name__ == "__main__":

    with timer("1. generator import 1000000 x 1000"):
        for idx, t in enumerate(get_trial_import(1000000, 1000)):
            a = t[0]
    print()

    with timer("1b. generator import 1000000 x 1000 file by file"):
        for idx, t in enumerate(get_trial_import_inc(1000000, 1000)):
            a = t[0]
    print()

    with timer("2. import 1000000 x 1000 with static import"):
        from trials.t_1000000 import trials
    print()

    with timer("3. import 1000000 x 1 (or 10)"):
        from trials.t_1000000x1.trials0 import trials
        for t in trials:
            a = t[0]
    print()

    with timer("4. generator import 1000000 x 1"):
        for t in get_trial_import(1000000, 1):
            a = t[0]
    print()

    with timer("5. generator import 1000000 x 10"):
        for t in get_trial_import(1000000, 10):
            a = t[0]
    print()

    with timer("6. import 1000000x10 splittrials (10 trials)"):
        from trials.t_1000000.splittrials0 import trials
    print()

    with timer("7. generator generate 1000000 x 10") as t1:
        for t in get_trial(1000000, 10):
            a = t[0]
    print("time per trial=%.4f\n"%(t1.total_time/10))

    with timer("8. generate 1000000 x 10") as t1:
        trials0 = numpy.array([gen_pos_numbers_inc_dec(1000000, up_chance=0.5) for i in range(10)])
        trials = [(min(trial), numpy.mean(trial), numpy.std(trial), trial) for trial in trials0]
    print("time per trial=%.4f\n"%(t1.total_time/10))

    with timer("9. simplejson 1000000 x 1"):
        with open("trials/t_1000000x1/trials0.json")as f:
            trials = json.load(f)
    print()

    with timer("10. simplejson 1000000 x 100"):
        with open("trials/t_1000000x100/trials0.json")as f:
            trials = simplejson.load(f)
    print()

    with timer("11. json 1000000 x 100"):
        with open("trials/t_1000000x100/trials1.json")as f:
            trials = json.load(f)
    print()

    with timer('12. read 1000000 x 10 from binary one by one'):
        with open('trials/trials_1000000x10.bin', 'rb') as file:
            for i in range(10000000):
                j = int.from_bytes(file.read(8), byteorder='big')
    print()

    with timer('read 1000000 x 10 from binary as struct'):
        ints_read = 0
        with open('trials/trials_1000000x10.bin', 'rb') as file:
            data = file.read()
            instruct = "Q" * ((len(data) ) // 8)
            d = struct.unpack("!"+instruct , data)
            iss = 0
            for i in d:
                iss += 1
    print()

    print("DONE")