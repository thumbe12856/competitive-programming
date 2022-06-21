from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def sovle(N, G):
    if N == 2:
        return 0

    def dfs(parent, node):
        if len(G[node]) == 1:
            return 0

        elif len(G[node]) == 2:
            return 1

        res = float('inf')
        for next_node in G[node]:
            if next_node == parent:
                continue

            res = min(res, dfs(node, next_node))

        return res + 2

    return N - dfs(0, 1) - 1

T = int(input())
for _ in range(T):
    N = int(input())
    G = defaultdict(set)
    G[1].add(0)
    for _ in range(N - 1):
        f, t = get_ints()
        G[f].add(t)
        G[t].add(f)

    print(sovle(N, G))
