from heapq import *
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

N = int(input())
q = []
for i in range(N):
    a, b = get_ints()
    q.append([b, a, i])

q.sort()
ans = 0
curr = 0
l, r = 0, N - 1
while l <= r:
    while l < len(q) and q[l][0] <= curr:
        if q[l][1] <= 0:
            l += 1
            continue

        ans += q[l][1]
        curr += q[l][1]
        q[l][1] = 0
        l += 1

    if q[r][1] <= 0:
        break

    target = q[l][0] - curr
    val = min(q[r][1], target)
    q[r][1] -= val
    curr += val
    ans += 2 * val
    if q[r][1] <= 0:
        r -= 1

print(ans)
