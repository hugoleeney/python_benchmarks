
from time import time
from scipy.special import comb as scipy_choose

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


with timer("scipy"):
    for i in range(1000):
        for j in range(i):
            scipy_choose(i,j)

