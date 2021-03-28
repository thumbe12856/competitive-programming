def solve(X, Y, S):
    N = len(S)
    for i in range(N):
        if S[i] == "C":
            S[i] = 0
        elif S[i] == "J":
            S[i] = 1
        else:
            S[i] = 2

    last_dp = {
        0: 0,
        1: 0,
    }
    for i in range(N - 2, -1, -1):
        dp = {
            0: float('inf'),
            1: float('inf'),
        }
        last_s = S[i + 1]
        s = S[i]
        if s == 2:
            if last_s == 1:
                dp[0] = X + last_dp[last_s] # CJ
                dp[1] = last_dp[last_s]     # JJ
            elif last_s == 0:
                dp[0] = last_dp[last_s]     # CC
                dp[1] = Y + last_dp[last_s] # JC
            else:
                dp[0] = min(
                    last_dp[0],     # CC
                    X + last_dp[1], # CJ
                )
                dp[1] = min(
                    Y + last_dp[0], # JC
                    last_dp[1],     # JJ
                )
        else:
            if last_s == 0 and s == 1:
                dp[s] = Y + last_dp[last_s]
            elif last_s == 1 and s == 0:
                dp[s] = X + last_dp[last_s]
            elif s != 2:
                if s == 0:
                    dp[s] = min(
                        X + last_dp[1], # CJ
                        last_dp[0],     # CC
                    )
                else:
                    dp[s] = min(
                        last_dp[1],     # JJ
                        Y + last_dp[0], # JC
                    )
            else:
                val = min(
                    last_dp[0], last_dp[1]
                )
                dp[0], dp[1] = val, val

        last_dp = dp.copy()

    if S[0] == 2:
        return min(last_dp[0], last_dp[1])
    return last_dp[S[0]]

T = int(input())
for test_num in range(T):
    X, Y, S = input().split()
    X, Y = int(X), int(Y)
    S = list(S)
    ans = solve(X, Y, S)
    print("Case #{}: {}".format(test_num + 1, ans))
