from collections import defaultdict

def solve(A, B, S):
    S = list(S)
    N = len(S)
    for i in range(N):
        if S[i] != "?":
            if S[-(i + 1)] != "?" and S[-(i + 1)] != S[i]:
                return -1
            S[-(i + 1)] = S[i]

    cs = defaultdict(int)
    for i in range(N):
        cs[S[i]] += 1
    if cs["0"] > A or cs["1"] > B:
        return -1
    elif cs["0"] + cs["?"] < A or cs["1"] + cs["?"] < B:
        return -1

    A -= cs["0"]
    B -= cs["1"]
    if (A & 1) and (B & 1):
        return -1

    if A & 1:
        if not (N & 1) or S[N // 2] != "?":
            return -1
        A -= 1
        S[N // 2] = 0

    if B & 1:
        if not (N & 1) or S[N // 2] != "?":
            return -1
        B -= 1
        S[N // 2] = 1

    idx = 0
    while A and idx < N:
        if S[idx] == "?" and S[-(idx + 1)] == "?":
            A -= 2
            S[idx] = 0
            S[-(idx + 1)] = 0

        idx += 1

    idx = 0
    while B and idx < N:
        if S[idx] == "?" and S[-(idx + 1)] == "?":
            B -= 2
            S[idx] = 1
            S[-(idx + 1)] = 1

        idx += 1

    for i in range(N):
        S[i] = str(S[i])

    if A == 0 and B == 0:
        ans = ("").join(S)
        return ans
    else:
        return -1

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    S = input()
    ans = solve(A, B, S)
    print(ans)
