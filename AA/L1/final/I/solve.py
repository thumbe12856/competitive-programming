from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

MOD = 998244353



N = int(input())
G = []
for _ in range(N):
    G.append(list(input().strip()))

def cal(vis, dirs, start, target):
    def dfs(i, j):
        if not (0 <= i < N and 0 <= j < N):
            return 0

        if (i, j) == target:
            return 1

        if G[i][j] == '#':
            return 0

        if (i, j) in vis:
            return vis[(i, j)]

        x1, y1 = dirs[0]
        x2, y2 = dirs[1]
        res = dfs(i + x1, j + y1) + dfs(i + x2, j + y2)
        vis[(i, j)] = res
        return vis[(i, j)]

    dfs(start[0], start[1])

rd = {}
cal(rd, [[0, 1], [1, 0]], [0, 0], (N - 1, N - 1))
lt = {}
cal(lt, [[0, -1], [-1, 0]], [N - 1, N - 1], (0, 0))

Q = int(input())
for _ in range(Q):
    x, y = get_ints()
    x -= 1
    y -= 1
    print((rd[(0, 0)] - (lt[x, y] * rd[(x, y)])) % MOD)
