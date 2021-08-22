from collections import defaultdict
import collections
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(G, Q, q):
    ans = [0] * Q
    vis = set()

    def dfs(node):
        vis.add(node)

        for x, idx in q[node]:
            if x in vis:
                ans[idx] = 1

        for next_node in G[node]:
            if next_node in vis:
                continue
            dfs(next_node)
        vis.remove(node)

    dfs(1)
    for i in range(Q):
        print(ans[i])

N = int(input())
G = defaultdict(set)
P = get_ints()
for i in range(len(P)):
    G[i + 2].add(P[i])
    G[P[i]].add(i + 2)

q = defaultdict(list)
Q = int(input())
for idx in range(Q):
    x, y = get_ints()
    q[y].append((x, idx))

solve(G, Q, q)
