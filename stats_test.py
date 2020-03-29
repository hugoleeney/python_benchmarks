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


assert math.isclose(statistics_mean, numpy_mean, abs_tol=1), "%s %s"%(statistics_mean, numpy_mean)

assert math.isclose(statistics_stdev, numpy_stddev, abs_tol=1), "%s %s"%(statistics_stdev, numpy_stddev)


'''
Sample Output:

timing: create array
runtime=32.42217493057251

timing: copy array
runtime=0.014689207077026367

timing: create numpy array
runtime=0.08298778533935547

timing: python min
python_min=0
runtime=0.019994020462036133

timing: statistics mean
statistics_mean=50041.906475
runtime=10.625783920288086

timing: statistics stddev
statistics_stdev=28843.027183552997
runtime=55.764643907547

timing: numpy min
numpy_min=0
runtime=0.006093025207519531

timing: numpy mean
50041.906475
runtime=0.0033330917358398438

timing: numpy stddev
28843.012762035803
runtime=0.00748896598815918

'''
