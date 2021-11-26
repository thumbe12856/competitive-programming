from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


cnt = defaultdict(int)
Q = int(input())
for _ in range(Q):
    Y, X = get_ints()
    if Y == 1:
        cnt[X] += 1
    elif Y == 2:
        if cnt[X]:
            cnt[X] -= 1
    else:
        print(cnt[X])
