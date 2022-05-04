from bisect import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N = int(input())
intervals_head, intervals_tail = [], []
for _ in range(N):
    f, t = get_ints()
    intervals_head.append((f, t))
    intervals_tail.append((t, f))

intervals_head.sort()
intervals_tail.sort()

N = int(input())
for _ in range(N):
    f, t = get_ints()
    l = bisect_left(intervals_head, f)
    r = bisect_left(intervals_tail, t)
    if r > len(intervals_tail):
        r -= 1
    if intervals_tail[]
