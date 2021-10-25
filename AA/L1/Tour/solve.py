import sys
from collections import defaultdict

sys.setrecursionlimit(10000)


def solve(N, G):
    def dfs(node):
        if node in vis:
            return

        vis.add(node)
        for next_node in G[node]:
            dfs(next_node)

    ans = 0
    for i in range(1, N + 1, 1):
        vis = set()
        dfs(i)
        ans += len(vis)

    return ans


G = defaultdict(set)
N, M = map(int, input().split())
for i in range(1, N + 1, 1):
    G[i].add(i)

for _ in range(M):
    f, t = map(int, input().split())
    G[f].add(t)

print(solve(N, G))
