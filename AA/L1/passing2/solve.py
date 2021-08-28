from collections import defaultdict
import collections
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(G, Q, q):
    ans = [0] * Q
    vis = set()

    def dfs(node, can):

        vis.add(node)
        for next_node in G[node]:
            can.add(next_node)

        for x, idx in q[node]:
            if x in can:
                ans[idx] = 1

        for next_node in G[node]:
            if next_node in vis:
                continue
            dfs(next_node, can)

        for next_node in G[node]:
            if next_node not in vis:
                can.remove(next_node)
        vis.remove(node)

    dfs(1, set([1]))
    for i in range(Q):
        print(ans[i])

N = int(input())
G = defaultdict(set)
for _ in range(N - 1):
    f, t = get_ints()
    G[f].add(t)
    G[t].add(f)

q = defaultdict(list)
Q = int(input())
for idx in range(Q):
    x, y = get_ints()
    q[y].append((x, idx))

solve(G, Q, q)
