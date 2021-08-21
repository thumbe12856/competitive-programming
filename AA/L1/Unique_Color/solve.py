from collections import defaultdict
import collections
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(G, C):
    ans = set()

    def dfs(node, vis, cnt):
        if cnt[C[node - 1]] == 0:
            ans.add(node)

        if node in vis:
            return

        vis.add(node)
        cnt[C[node - 1]] += 1
        for next_node in G[node]:
            dfs(next_node, vis, cnt)
        cnt[C[node - 1]] -= 1
        vis.remove(node)

    cnt = collections.defaultdict(int)
    dfs(1, set(), cnt)
    for node in ans:
        print(node)

N = int(input())
C = get_ints()
G = defaultdict(set)
for _ in range(N - 1):
    f, t = get_ints()
    G[f].add(t)
    G[t].add(f)
solve(G, C)
