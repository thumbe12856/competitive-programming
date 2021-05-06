import sys
from sys import exit


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N, T = map(int, input().split())
K = int(input())
l, r = 0, N - 1
last = 0
while l < r:
    mid = (l + r) // 2
    print("? {} {}".format(l + 1, mid + 1))
    sys.stdout.flush()
    ret = int(input())
    if ret == -1:
        exit()

    cnt = last + mid - l + 1 - ret
    if cnt < K:
        last += cnt - last
        l = mid + 1
    else:
        r = mid

print("! {}".format(l + 1))
sys.stdout.flush()
