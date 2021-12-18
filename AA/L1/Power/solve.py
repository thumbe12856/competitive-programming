from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(cnt):
    ans = 0
    last = 0
    presum = defaultdict(int)
    for i in range(len(cnt)):
        last += cnt[i]
        presum[last] += 1

    for n in presum:
        ans += n * n * presum[n]
    return ans


cnt = [0] * (10 ** 6 + 1)
N = int(input())
for _ in range(N):
    l, r = get_ints()
    cnt[l] += 1
    cnt[r] -= 1

print(solve(cnt))
