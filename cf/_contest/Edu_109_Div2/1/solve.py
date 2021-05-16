import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N):
    ori = 100
    for idx in range(2, 101, 1):
        while N % idx == 0 and ori % idx == 0:
            N //= idx
            ori //= idx

    return ori

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
