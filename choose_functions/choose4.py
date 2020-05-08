def choose4(n, k):
    if k == n: return 1
    if k > n: return 0
    d, q = max(k, n-k), min(k, n-k)
    num =  1
    for n in range(d+1, n+1): num *= n
    denom = 1
    for d in range(1, q+1): denom *= d
    return num / denom