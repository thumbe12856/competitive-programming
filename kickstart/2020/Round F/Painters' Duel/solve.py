from functools import lru_cache

T = int(input())

def solve(S, x1, y1, x2, y2, vis):

    def dfs(turn, x1, y1, x2, y2, vis, a, b):
        # print(turn, x1, y1, x2, y2, a, b)
        # for i in range(len(vis)):
        #     print(vis[i])

        A_can = set()
        B_can = set()

        # A turn
        # left
        if 1 <= x1 - 1 and vis[y1][x1 - 1] == 0:
            A_can.add((y1, x1 - 1))

        # rigth
        if x1 + 1 <= y1 * 2 - 1 and vis[y1][x1 + 1] == 0:
            A_can.add((y1, x1 + 1))

        # down
        if x1 & 1:
            if y1 + 1 <= S and x1 + 1 <= (y1 + 1) * 2 - 1 and vis[y1 + 1][x1 + 1] == 0:
                A_can.add((y1 + 1, x1 + 1))

        # up
        else:
            if y1 - 1 >= 1 and x1 - 1 >= 1 and vis[y1 - 1][x1 - 1] == 0:
                A_can.add((y1 - 1, x1 - 1))

        # B turn
        # left
        if 1 <= x2 - 1 and vis[y2][x2 - 1] == 0:
            B_can.add((y2, x2 - 1))

        # rigth
        if x2 + 1 <= y2 * 2 - 1 and vis[y2][x2 + 1] == 0:
            B_can.add((y2, x2 + 1))

        # down
        if x2 & 1:
            if y2 + 1 <= S and x2 + 1 <= (y2 + 1) * 2 - 1 and vis[y2 + 1][x2 + 1] == 0:
                B_can.add((y2 + 1, x2 + 1))

        # up
        else:
            if y2 - 1 >= 1 and x2 - 1 >= 1 and vis[y2 - 1][x2 - 1] == 0:
                B_can.add((y2 - 1, x2 - 1))

        if not A_can and not B_can:
            return a - b

        max_val = float('-inf')
        min_val = float('inf')
        if turn == 0:
            if A_can:
                for next_y, next_x in A_can:
                    vis[next_y][next_x] = 2
                    max_val = max(max_val, dfs(1 - turn, next_x, next_y, x2, y2, vis, a + 1, b))
                    vis[next_y][next_x] = 0
            else:
                max_val = dfs(1 - turn, x1, y1, x2, y2, vis, a, b)
            res = max_val
        else:
            if B_can:
                for next_y, next_x in B_can:
                    vis[next_y][next_x] = 3
                    min_val = min(min_val, dfs(1 - turn, x1, y1, next_x, next_y, vis, a, b + 1))
                    vis[next_y][next_x] = 0
            else:
                min_val = dfs(1 - turn, x1, y1, x2, y2, vis, a, b)
            res = min_val

        return res

    return dfs(0, x1, y1, x2, y2, vis, 0, 0)

for sample_num in range(T):
    S, y1, x1, y2, x2, C = list(map(int, input("").split()))
    vis = [[0 for i in range(S * 2)] for j in range(S + 1)]
    vis[y1][x1] = 2
    vis[y2][x2] = 3

    for i in range(C):
        y, x = map(int, input("").split())
        vis[y][x] = 1

    for i in range(len(vis[0])):
        vis[0][i] = 1
    for i in range(1, S + 1):
        vis[i][0] = 1
        for j in range(i * 2, len(vis[i])):
            vis[i][j] = 1

    ans = solve(S, x1, y1, x2, y2, vis)
    print("Case #{0}: {1}".format(sample_num + 1, ans))
