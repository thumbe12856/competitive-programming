import sys

K = int(input())
two_K = 1 << K
S = list(sys.stdin.readline()[:-1])
dp = [1] * (two_K << 1)

for i in range(two_K - 1, 0, -1):
    c = S[two_K - i - 1]
    if c == "1":
        dp[i] = dp[i << 1]
    elif c == "0":
        dp[i] = dp[(i << 1) + 1]
    else:
        dp[i] = dp[i << 1] + dp[(i << 1) + 1]

Q = int(input())
ans = []

for _ in range(Q):
    match_number, winner = sys.stdin.readline().strip().split()
    match_number = int(match_number) - 1
    S[match_number] = winner

    i = two_K - match_number - 1
    while i:
        c = S[two_K - i - 1]
        if c == "1":
            dp[i] = dp[i << 1]
        elif c == "0":
            dp[i] = dp[(i << 1) + 1]
        else:
            dp[i] = dp[i << 1] + dp[(i << 1) + 1]

        i //= 2

    ans.append(dp[1])

for a in ans:
    print(a)
