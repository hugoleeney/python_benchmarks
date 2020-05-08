'''
timing: scipy
runtime=0.8869051933288574

timing: sympy
runtime=451.0642590522766

timing: gmpy
runtime=9.880879878997803

timing: choose1
runtime=0.03794503211975098

'''

from time import time
from scipy.special import comb as scipy_choose
from sympy import binomial as sympy_choose
from gmpy import comb

from choose_functions.choose1 import choose1
from choose_functions.choose2 import choose2
from choose_functions.choose3 import choose3
from choose_functions.choose4 import choose4
from choose_functions.choose5 import choose5
from choose_functions.choose6 import choose6


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
    for i in range(0, 10000,100):
        for j in range(0,i,10):
            scipy_choose(i,j)

with timer("sympy"):
    for i in range(0, 10000,100):
        for j in range(0,i,10):
            sympy_choose(i,j)

with timer("gmpy"):
    for i in range(0, 10000,100):
        for j in range(0,i,10):
            comb(i,j)

with timer("choose1"):
    for i in range(0, 10000,100):
        for j in range(0,i,10):
            choose1(i,j)


# OverflowError: integer division result too large for a float
# with timer("choose2"):
#     for i in range(0, 10000,100):
#         for j in range(0,i,10):
#             choose2(i,j)

# tooooo slow
# with timer("choose3"):
#     for i in range(0, 10000,100):
#         for j in range(0,i,10):
#             choose3(i,j)

# OverflowError: integer division result too large for a float
# with timer("choose4"):
#     for i in range(0, 10000,100):
#         for j in range(0,i,10):
#             choose4(i,j)

# RecursionError: maximum recursion depth exceeded in comparison
# with timer("choose5"):
#     for i in range(0, 10000,100):
#         for j in range(0,i,10):
#             choose5(i,j)
#             choose5.cache_clear()

# OverflowError: integer division result too large for a float
# with timer("choose6"):
#     for i in range(0, 10000,100):
#         for j in range(0,i,10):
#             choose6(i,j)
