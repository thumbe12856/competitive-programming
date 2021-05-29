from bisect import *

LIMIT = 10 ** 9 * 2
can = []
val = 1
while val < LIMIT:
    can.append(val)
    val *= 2

T = int(input())
for _ in range(T):
    N = int(input())
    idx = bisect_left(can, N)
    if can[idx] > N:
        idx -= 1
    print(can[idx] - 1)
