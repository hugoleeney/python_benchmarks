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


def use_random(x):
    results = 0
    for i in range(x):
        if random.random() < 0.5:
            results += 1
    return results


def use_choice(x):
    results = 0
    for i in range(x):
        if random.choice([0,1]):
            results += 1
    return results


with timer("use_random"):
    print(use_random(10000000))


with timer("use_choice"):
    print(use_choice(10000000))


'''
SAMPLE OUTPUT

timing: use_random
4999421
runtime=2.049018144607544

timing: use_choice
5001631
runtime=16.556126832962036
'''
