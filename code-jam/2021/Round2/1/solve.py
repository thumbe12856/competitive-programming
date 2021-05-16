from collections import defaultdict, deque
from functools import lru_cache
from heapq import *
from itertools import product, permutations
import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N):
    for i in range(N - 1):
        print("M {} {}".format(i + 1, N))
        sys.stdout.flush()

        res = int(input())

        # with open("temp.txt", "a") as f:
        #     f.writelines("M {} {}, res: {}\n".format(i + 1, N, res))

        if res == -1:
            sys.exit()

        if i + 1 == res:
            continue

        print("S {} {}".format(i + 1, res))
        # with open("temp.txt", "a") as f:
        #     f.writelines("S {} {}\n".format(i + 1, res))
        sys.stdout.flush()

        res = int(input())
        if res == -1:
            sys.exit()

    print("D")
    sys.stdout.flush()
    res = int(input())

    # with open("temp.txt", "a") as f:
    #     f.writelines("D, res:{}\n".format(res))

    if res == -1:
        sys.exit()

T, N = map(int, input().split())
for _ in range(T):
    solve(N)


# s = 0
# for i in range(2, 101, 1):
#     s += 10 ** 8 / i
# print(s, s < 6 * 10 ** 8)
