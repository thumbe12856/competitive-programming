from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, G):
    def dfs(node, mud):
        if (node, mud) in vis:
            return

        vis.add((node, mud))
        vis_node.add(node)
        for next_node, need_mud in G[node]:
            if need_mud == 0:
                dfs(next_node, mud)
            else:
                if mud == 1:
                    dfs(next_node, 0)

    ans = 0
    for i in range(1, N + 1, 1):
        vis = set()
        vis_node = set()
        dfs(i, 1)
        ans += len(vis_node)

    return ans

G = defaultdict(set)
N, M = get_ints()
for _ in range(M):
    a, b, c = get_ints()
    G[a].add((b, c))

print(solve(N, G))
