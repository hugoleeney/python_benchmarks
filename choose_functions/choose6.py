def choose6(n,k): #computes nCk, the number of combinations n choose k
    result = 1
    for i in range(n):
        result*=(i+1)
    for i in range(k):
        result/=(i+1)
    for i in range(n-k):
        result/=(i+1)
    return result