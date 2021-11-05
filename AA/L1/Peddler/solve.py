from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(200010)


def solve(N, M, G, nums):
    ans = float('-inf')

    vis = {}
    def dfs(f):
        if f in vis:
            return vis[f]

        max_val = nums[f]

        for t in G[f]:
            max_val = max(
                max_val, dfs(t)
            )

        vis[f] = max_val
        return vis[f]

    for f in range(N):
        for t in G[f]:
            ans = max(ans, dfs(t) - nums[f])

    return ans


G = defaultdict(set)
N, M = get_ints()
nums = get_ints()
for _ in range(M):
    f, t = get_ints()
    f -= 1
    t -= 1
    G[f].add(t)

print(solve(N, M, G, nums))
