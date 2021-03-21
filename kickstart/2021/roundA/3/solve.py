from heapq import *

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def solve(R, C, G):
    ans = 0
    q = []
    for i in range(R):
        for j in range(C):
            heappush(q, (-G[i][j], i, j))

    vis = set()
    while q:
        v, i, j = heappop(q)
        if (i, j) in vis:
            continue

        v = -v
        vis.add((i, j))
        for x, y in dirs:
            if not(0 <= i + x < R and 0 <= j + y < C):
                continue

            elif (i + x, j + y) in vis:
                continue

            diff = abs(G[i][j] - G[i + x][j + y])
            if diff <= 1:
                continue

            next_diff = abs(v - 1 - G[i + x][j + y])
            G[i + x][j + y] = v - 1
            ans += next_diff
            heappush(q, (-G[i + x][j + y], i + x, j + y))

    return ans

T = int(input())
for num_test_cases in range(T):
    R, C = map(int, input().split())
    G = []
    for i in range(R):
        G.append(list(map(int, input().split())))
    ans = solve(R, C, G)
    print("Case #{}: {}".format(num_test_cases + 1, ans))
