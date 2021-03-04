from bisect import bisect_left, bisect_right
import math
from collections import Counter
import operator as op
from functools import reduce

def comb(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

T = int(input())
M = 10 ** 9 + 7
for _ in range(T):
    n, k = input().split()
    n, k = int(n), int(k)
    A = list(map(int, input().split()))
    A.sort()
    N = len(A)
    target = A[N - k]
    l = bisect_left(A, target)
    r = bisect_right(A, target)
    m = r - l
    c = r - 1 - (N - k) + 1
    print(comb(m, c) % M)
