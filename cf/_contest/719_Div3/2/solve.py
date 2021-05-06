from bisect import bisect_left
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

vis = []
for i in range(1, 12, 1):
    for j in range(1, 10, 1):
        curr = int(str(j) * i)
        vis.append(curr)

vis.sort()

T = int(input())
for _ in range(T):
    N = int(input())
    idx = bisect_left(vis, N)
    if N >= vis[idx]:
        print(idx + 1)
    else:
        print(idx)
