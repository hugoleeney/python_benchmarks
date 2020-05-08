from functools import lru_cache

@lru_cache(maxsize=None)
def choose5(n, r):
    return 1 if r == 0 or r == n else choose5(n - 1, r - 1) + choose5(n - 1, r)
