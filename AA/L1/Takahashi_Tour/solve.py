from collections import defaultdict


def solve(G):
    for node in G:
        G[node].sort()

    ans = []
    vis = set()
    def dfs(node):
        ans.append(node)
        vis.add(node)
        for next_node in G[node]:
            if next_node in vis:
                continue
            dfs(next_node)
            ans.append(node)

    dfs(1)
    print(*ans)

G = defaultdict(list)
N = int(input())
for _ in range(N - 1):
    f, t = map(int, input().split())
    G[f].append(t)
    G[t].append(f)

solve(G)
