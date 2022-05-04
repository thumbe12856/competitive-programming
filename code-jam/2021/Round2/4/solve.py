from collections import defaultdict, deque
from functools import lru_cache
from heapq import *
from itertools import product, permutations
import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, K, nums):

T = int(input())
for case_num in range(T):
    N, K = get_ints()
    nums = get_ints()
    ans = solve(N, K, nums)
    print("Case #{}: {}".format(case_num + 1, ans))
