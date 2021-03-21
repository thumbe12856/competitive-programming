import time
from functools import lru_cache
from collections import defaultdict

def solve(N, G, cost):
    cnt = 0
    can = []
    for i in range(N):
        for j in range(N):
            if G[i][j] == -1:
                cnt += 1
                can.append((i, j))

    if cnt < 4:
        return 0

    def check(mask):
        valid = False
        while not valid:
            valid = True
            R, C = defaultdict(set), defaultdict(set)
            for i in range(len(can)):
                ii, jj = can[i]
                if not ((1 << i) & mask):
                    R[ii].add(i)
                    C[jj].add(i)

            for i in R:
                if len(R[i]) <= 1:
                    for j in R[i]:
                        mask |= (1 << j)
                        valid = False

            for i in C:
                if len(C[i]) <= 1:
                    for j in C[i]:
                        mask |= (1 << j)
                        valid = False

        for i in R:
            if len(R[i]) >= 2:
                return float('inf')

        for i in C:
            if len(C[i]) >= 2:
                return float('inf')

        return 0

    @lru_cache(None)
    def dfs(mask):
        res = check(mask)
        if res != float('inf'):
            return res

        min_cost = float('inf')
        for i in range(len(can)):
            if (1 << i) & mask:
                continue

            ii, jj = can[i]
            min_cost = min(
                min_cost,
                cost[ii][jj] + dfs((1 << i) | mask)
            )
        return min_cost

    ans = dfs(0)
    dfs.cache_clear()

    return ans

s = time.time()
T = int(input())
for num_test_cases in range(T):
    N = int(input())

    G = []
    for i in range(N):
        G.append(list(map(int, input().split())))

    cost = []
    for i in range(N):
        cost.append(list(map(int, input().split())))

    input()
    input()

    ans = solve(N, G, cost)
    print("Case #{}: {}".format(num_test_cases + 1, ans))
e = time.time()
# print(e - s)
