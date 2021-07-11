import sys
sys.setrecursionlimit(4 * 10 ** 5)
from bisect import *
from collections import defaultdict
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, G):
    ans = [0] * N
    can = set()
    all_vis = defaultdict(int)
    def dfs(node, vis):
        if node in vis:
            ans[node] = -1
            can.add(node)
            all_vis[node] = 2
            return

        if all_vis[node] >= 2:
            return

        all_vis[node] += 1
        vis.add(node)
        ans[node] = min(2, ans[node] + 1)
        for next_node in G[node]:
            dfs(next_node, vis)
        vis.remove(node)

    dfs(0, set())

    all_vis = set()
    def dfs2(node, vis):
        if node in vis:
            return

        if node in all_vis:
            return

        ans[node] = -1
        vis.add(node)
        all_vis.add(node)
        for next_node in G[node]:
            dfs2(next_node, vis)
        vis.remove(node)

    for node in can:
        dfs2(node, set())

    return (" ").join(map(str, ans))

T = int(input())
for _ in range(T):
    input()
    N, M = get_ints()
    G = defaultdict(set)
    for i in range(M):
        f, t = get_ints()
        f -= 1
        t -= 1
        G[f].add(t)
    print(solve(N, G))
