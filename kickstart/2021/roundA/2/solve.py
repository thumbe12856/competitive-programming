from collections import defaultdict

def solve(R, C, G):
    # 0: up, 1: down, 2: left, 3: right
    dp = [[[0, 0, 0, 0] for i in range(C)] for j in range(R)]

    for i in range(R):
        for j in range(C):
            if G[i][j] == "1":
                dp[i][j][0] = 1 + dp[i - 1][j][0]
                dp[i][j][2] = 1 + dp[i][j - 1][2]
    for i in range(R - 1, -1, -1):
        for j in range(C - 1, -1, -1):
            if G[i][j] == "1":
                dp[i][j][1] = 1 + dp[(i + 1) % R][j][1]
                dp[i][j][3] = 1 + dp[i][(j + 1) % C][3]

    ans = 0
    for i in range(R):
        for j in range(C):
            if G[i][j] == "1":
                # up: L, right: W
                if dp[i][j][3] >= 2:
                    ans += max(0, min(dp[i][j][0] // 2, dp[i][j][3]) - 1)
                # up: W, right: L
                if dp[i][j][0] >= 2:
                    ans += max(0, min(dp[i][j][0], dp[i][j][3] // 2) - 1)

                # up: L, left: W
                if dp[i][j][2] >= 2:
                    ans += max(0, min(dp[i][j][0] // 2, dp[i][j][2]) - 1)
                # up: W, left: L
                if dp[i][j][0] >= 2:
                    ans += max(0, min(dp[i][j][0], dp[i][j][2] // 2) - 1)

                # down: L, right: W
                if dp[i][j][3] >= 2:
                    ans += max(0, min(dp[i][j][1] // 2, dp[i][j][3]) - 1)
                # down: W, right: L
                if dp[i][j][1] >= 2:
                    ans += max(0, min(dp[i][j][1], dp[i][j][3] // 2) - 1)

                # down: L, left: W
                if dp[i][j][2] >= 2:
                    ans += max(0, min(dp[i][j][1] // 2, dp[i][j][2]) - 1)
                # down: W, left: L
                if dp[i][j][1] >= 2:
                    ans += max(0, min(dp[i][j][1], dp[i][j][2] // 2) - 1)

    return ans

T = int(input())
for num_test_cases in range(T):
    R, C= map(int, input().split())
    G = []
    for i in range(R):
        G.append(input().split())
    ans = solve(R, C, G)
    print("Case #{}: {}".format(num_test_cases + 1, ans))
