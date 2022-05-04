from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    ans = float('inf')
    can = defaultdict(int)
    vis = {}
    def dfs(idx, curr, curr_res):
        nonlocal ans

        key = (idx, curr, curr_res)

        if idx >= N:
            ans = min(ans, curr_res)
            vis[key] = curr_res
            return vis[key]

        if curr_res >= ans:
            vis[key] = float('inf')
            return vis[key]

        if key in vis:
            return vis[key]

        val = curr + nums[idx]
        can[val] += 1
        if can[val] == 1:
            res1 = dfs(idx + 1, val, curr_res + 1)
        else:
            res1 = dfs(idx + 1, val, curr_res)
        can[val] -= 1

        val = curr - nums[idx]
        can[val] += 1
        if can[val] == 1:
            res2 = dfs(idx + 1, val, curr_res + 1)
        else:
            res2 = dfs(idx + 1, val, curr_res)
        can[val] -= 1

        vis[key] = min(res1, res2)
        return vis[key]

    can[0] = 1
    return dfs(0, 0, 1)

N = int(input())
nums = get_ints()
print(solve(N, nums))
