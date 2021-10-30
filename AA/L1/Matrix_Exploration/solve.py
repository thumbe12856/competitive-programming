import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, M, K, G, special_points):
    ans = 0
    q = special_points
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    vis = set()
    while q:
        next_q = []
        for i, j, d in q:

            if (i, j) in vis:
                continue

            vis.add((i, j))
            ans += d
            for x, y in dirs:
                if  0 <= i + x < M and\
                    0 <= j + y < N and\
                    G[i + x][j + y] == '.' and\
                    (i + x, j + y) not in vis:
                    next_q.append((i + x, j + y, d + 1))

        q = next_q

    return ans

M, N, K = get_ints()
G = []
special_points = set()
for _ in range(M):
    G.append(input())

for _ in range(K):
    i, j = get_ints()
    special_points.add((i - 1, j - 1, 0))

print(solve(N, M, K, G, special_points))
