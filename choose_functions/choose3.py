def choose3(n, k):
    """ (int, int) -> int

             | c(n-1, k-1) + c(n-1, k), if 0 < k < n
    c(n,k) = | 1                      , if n = k
             | 1                      , if k = 0

    Precondition: n > k

    >>> binomial(9, 2)
    36
    """

    c = [0] * (n + 1)
    c[0] = 1
    for i in range(1, n + 1):
        c[i] = 1
        j = i - 1
        while j > 0:
            c[j] += c[j - 1]
            j -= 1

    return c[k]