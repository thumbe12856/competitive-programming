from bisect import bisect_left
from collections import Counter
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

T = int(input())
for _ in range(T):
    N, K = get_ints()
    nums = get_ints()
    weight = get_ints()
    one, two = [], []
    for i in range(N):
        if weight[i] == 1:
            one.append(nums[i])
        else:
            two.append(nums[i])

    one.sort(reverse=True)
    two.sort(reverse=True)
    o_presum, t_presum = [0], [0]
    for i in range(len(one)):
        o_presum.append(one[i] + o_presum[-1])
    for i in range(len(two)):
        t_presum.append(two[i] + t_presum[-1])

    # print(o_presum)
    # print(t_presum)
    ans = float('inf')
    for i in range(len(t_presum)):
        target = K - t_presum[i]
        idx = bisect_left(o_presum, target)
        if idx < len(o_presum) and o_presum[idx] + t_presum[i] >= K:
            ans = min(ans, i * 2 + idx)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
