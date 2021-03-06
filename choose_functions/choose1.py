import operator as op
from functools import reduce

# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def choose1(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
