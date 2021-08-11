def solve(N):
    ans = 0
    for i in range(1, 101, 1):
        for j in range(1, 101, 1):
            for valid, k in [
                [True, N - i - j],                # a + b + c
                [True, N - i * j],                # a * b + c
                [not((N - i) % j), (N - i) // j], # a + b * c
                [not(N % (i * j)), N // (i * j)], # a * b * c
            ]:
                if valid and 1 <= k <= 100:
                    ans += 1
    return ans

dp = [0] * (100 ** 3 + 1)
for i in range(1, 101, 1):
    for j in range(1, 101, 1):
        for k in range(1, 101, 1):
            dp[i + j + k] += 1
            dp[i + j * k] += 1
            dp[i * j + k] += 1
            dp[i * j * k] += 1

def solve2(N):
    return dp[N]

Q = int(input())
for _ in range(Q):
    N = int(input())
    print(solve2(N))
