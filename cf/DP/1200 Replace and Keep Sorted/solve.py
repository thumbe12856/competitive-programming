from functools import lru_cache
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N, Q, K = get_ints()
nums = get_ints()
nums = [0] + nums + [K + 1]

presum = [0]
v = 0
for i in range(1, N + 1):
    v += nums[i + 1] - nums[i - 1] - 1 - 1
    presum.append(v)

for _ in range(Q):
    l, r = get_ints()

    # l + 1 ~ r - 1
    ans = presum[r - 1] - presum[l]

    # l
    upper, lower = nums[l + 1], 0
    ans += upper - lower - 1 - 1

    # r
    upper, lower = K + 1, nums[r - 1]
    ans += upper - lower - 1 - 1

    print(ans)
