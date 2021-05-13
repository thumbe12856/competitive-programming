import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def print_result(ans):
    for i in range(len(ans)):
        print((" ").join(map(str, ans[i])))

def solve(N, M, K, hor, ver):
    if K & 1:
        print_result([[-1 for i in range(N)] for j in range(M)])
        return

    grid = [[0 for i in range(N)] for j in range((M))]
    def cal(i, j):
        can = set()
        if j > 0:
            can.add(
                2 * hor[i][j - 1] + grid[i][j - 1]
            )
        if j + 1 < N:
            can.add(
                2 * hor[i][j] + grid[i][j + 1]
            )
        if i > 0:
            can.add(
                2 * ver[i - 1][j] + grid[i - 1][j]
            )
        if i + 1 < M:
            can.add(
                2 * ver[i][j] + grid[i + 1][j]
            )
        return min(can)

    for _ in range(K // 2):
        next_grid = [[0 for i in range(N)] for j in range(M)]
        for i in range(M):
            for j in range(N):
                next_grid[i][j] = cal(i, j)
        grid = next_grid

    print_result(grid)

M, N, K = map(int, input().split())
hor = []
ver = []
for i in range(M):
    nums = get_ints()
    hor.append(nums)

for i in range(M - 1):
    nums = get_ints()
    ver.append(nums)

solve(N, M, K, hor, ver)
