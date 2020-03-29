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


'''
SAMPLE OUTPUT

timing: use_random
4999421
runtime=2.049018144607544

timing: use_choice
5001631
runtime=16.556126832962036
'''
