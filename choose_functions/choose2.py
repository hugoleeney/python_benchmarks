from math import factorial as f

def choose2(n,r):
    return f(n) / f(r) / f(n-r)
