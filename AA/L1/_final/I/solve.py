import sys
from collections import defaultdict
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)
MOD = 998244353


lt = defaultdict(lambda: defaultdict(int))
rd = defaultdict(lambda: defaultdict(int))
def cal(G, N):
    lt[1][1] = 1
    for i in range(1, N + 1, 1):
        for j in range(1, N + 1, 1):
            if(G[i - 1][j - 1] == "." and i + j != 2):
                lt[i][j] = (lt[i][j - 1] + lt[i - 1][j]) % MOD

    rd[N][N] = 1
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            if(G[i - 1][j - 1] == "." and i + j != N * 2):
                rd[i][j] = (rd[i][j + 1] + rd[i + 1][j]) % MOD

G = []
N = int(input())
for _ in range(N):
    G.append(list(input().strip()))

cal(G, N)

Q = int(input())
for _ in range(Q):
    x, y = get_ints()
    print((lt[N][N] - (rd[x][y] * lt[x][y])) % MOD)

