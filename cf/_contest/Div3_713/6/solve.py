import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, C, A, B):
    ans = float('inf')
    curr_day, money = 0, 0
    for i in range(len(B)):
        ans = min(ans, math.ceil((C - money) / A[i]) + curr_day)
        m = math.ceil((B[i] - money) / A[i])
        print(B[i], money, m)
        money += m * A[i] - B[i]
        curr_day += 1 + m

    ans = min(ans, math.ceil((C - money) / A[-1]) + curr_day)
    return ans

T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    A = get_ints()
    B = get_ints()
    print(solve(N, C, A, B))
