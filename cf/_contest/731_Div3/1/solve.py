from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

T = int(input())
for _ in range(T):
    input()
    ax, ay = get_ints()
    bx, by = get_ints()
    fx, fy = get_ints()

    ans = abs(ax - bx) + abs(ay - by)
    if (ax == bx == fx and (ay <= fy <= by or ay >= fy >= by)) or \
        (ay == by == fy and (ax <= fx <= bx or ax >= fx >= bx)):
        ans += 2
    print(ans)
