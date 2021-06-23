import math
from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(A, B, K):
    if K == 1:
        if A != B and (A % B == 0 or B % A == 0):
            return "YES"
        return "NO"

    def cal(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1

        cnt = 0
        target = math.ceil(math.sqrt(n))
        while not (n & 1):
            n //= 2
            cnt += 1

        i = 3
        while i <= n and i <= target:
            if n % i == 0:
                n //= i
                cnt += 1
            else:
                i += 2

        if n != 1:
            cnt += 1
        return cnt

    def cal2(n):
        cnt = 0
        while not (n & 1):
            n //= 2
            cnt += 1
        i = 3
        while i <= n:
            if n % i == 0:
                n //= i
                cnt += 1
            else:
                i += 2
        return cnt


    cnt_a = cal(A)
    cnt_b = cal(B)
    if cnt_a + cnt_b >= K:
        return "YES"
    return "NO"

T = int(input())
for _ in range(T):
    A, B, K = get_ints()
    print(solve(A, B, K))
