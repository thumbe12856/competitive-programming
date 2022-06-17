from collections import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(G, M, N):
    vis = defaultdict(int)

    def dfs(target, i, j):
        if not (0 <= i < M and 0 <= j < N):
            return

        if G[i][j] == '.' or G[i][j] != target:
            return

        G[i][j] = '.'
        dfs(target, i + 1, j)
        dfs(target, i, j + 1)
        dfs(target, i - 1, j)
        dfs(target, i, j - 1)

    for i in range(M):
        for j in range(N):
            c = G[i][j]
            if c == '.':
                continue
            dfs(c, i, j)
            vis[c] += 1

    sorted_key = sorted(vis.keys(), key=lambda c: (-vis[c], c))
    for c in sorted_key:
        print("{}: {}".format(c, vis[c]))

T = int(input())
for _ in range(T):
    print("World #{}".format(_ + 1))
    M, N = get_ints()
    G = []
    for i in range(M):
        G.append(list(input().strip()))

    solve(G, M, N)

