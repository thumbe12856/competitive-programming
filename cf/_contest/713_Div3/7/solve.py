from collections import defaultdict


dp = defaultdict(int)
M = 10 ** 7 + 1
for i in range(1, M + 1, 1):
    for j in range(i, M + 1, i):
        dp[j] += i

dp2 = {}
for i in range(1, M + 1, 1):
    if dp[i] < M:
        dp2[dp[i]] = i

T = int(input())
for _ in range(T):
    N = int(input())
    if N in dp2:
        print(dp2[N])
    else:
        print(-1)
