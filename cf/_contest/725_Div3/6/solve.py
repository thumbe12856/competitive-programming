from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

T = int(input())
for _ in range(T):
    l, r = get_ints()
    ans = 0
    while l or r:
        ans += r - l
        r //= 10
        l //= 10
    print(ans)
