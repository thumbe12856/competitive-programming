import json

from functools import lru_cache
from collections import defaultdict

def solve(nums, N):
    # @lru_cache(None)
    def dfs(arr, val):
        if len(arr) == 1:
            return val, 1

        ret_val, ret_cnt = 0, 0
        before, after = [], arr[1:]
        for i in range(len(arr) - 1):
            if i > 0:
                before += [arr[i - 1]]
            if i + 1 < len(arr):
                after = after[1:]

            temp_val, cnt = dfs(
                tuple(list(before) + [arr[i] + arr[i + 1]] + list(after)),
                val + arr[i] + arr[i + 1]
            )
            ret_cnt += cnt
            ret_val += temp_val
        return ret_val, ret_cnt

    ans, cnt = dfs(tuple(nums), 0)
    print(ans, cnt)
    return ans / cnt

# T = int(input())
# for t in range(T):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     ans = solve(nums, N)
#     print("Case #{}: {}".format(t + 1, ans))

def test():
    arr = [19, 3, 78, 2, 31]
    target = 8456
    for a in range(40, 80, 1):
        for b in range(40, 80, 1):
            for c in range(40, 80, 1):
                for d in range(40, 80, 1):
                    for e in range(40, 80, 1):
                        v = a * 19 + b * 3 + c * 78 + d * 2 + e * 31
                        if v == target and a == e and b == d and a < b < c:
                            print(a, b, c, d, e)
                        elif v >= target:
                            break
test()
