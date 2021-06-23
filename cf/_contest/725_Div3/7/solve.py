from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(x, y, a, b):
    if a == b:
        return min(x, y) // a

    ans = 0
    target_max = max(a, b)
    target_min = min(a, b)
    if x < y:
        x, y = y, x

    if max(x, y) < target_max or min(x, y) < target_min:
        return ans

    max_t = min(x // target_max, y // target_min)
    t = min(max_t, (x - y - 1) // (target_max - target_min))
    x -= target_max * t
    y -= target_min * t
    ans = t
    if max(x, y) < target_max or min(x, y) < target_min:
        return ans

    t = y // (a + b)
    temp_ans = t * 2
    x -= (a + b) * t
    y -= (a + b) * t
    temp_ans += min(x // target_max, y // target_min)
    ans += temp_ans

    return ans

T = int(input())
for _ in range(T):
    x, y, a, b = get_ints()
    print(solve(x, y, a, b))
