import sys
from collections import defaultdict

sys.setrecursionlimit(100001)


def solve(G):
    vis = defaultdict(int)
    def dfs(start, node):
        if vis[node] == 1:
            path.append(node)
            return True
        elif vis[node] == 2:
            return False

        vis[node] = 1
        path.append(node)
        for next_node in G[node]:
            if dfs(start, next_node):
                return True

        vis[node] = 2
        path.pop()
        return False

    for f in list(G.keys()):
        path = [f]
        for t in G[f]:
            vis[f] = 1
            if dfs(f, t):
                res = [path[-1]]
                for i in range(len(path) - 2, -1, -1):
                    res.append(path[i])
                    if path[i] == res[0]:
                        return res[::-1]

    return None

G = defaultdict(set)
N, M = map(int, input().split())

for _ in range(M):
    f, t = map(int, input().split())
    G[f].add(t)

res = solve(G)
if res:
    print(len(res))
    print(*res)
else:
    print("IMPOSSIBLE")
