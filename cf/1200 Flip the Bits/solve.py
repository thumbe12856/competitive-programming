def solve(N, S, P):
    cs = [[0, 0] for _ in range(N)]
    for i in range(N):
        cs[i][0] = cs[i - 1][0]
        cs[i][1] = cs[i - 1][1]
        cs[i][int(S[i])] += 1

    flip_time = 0
    for i in range(N - 1, -1, -1):
        if (S[i] != P[i] and not (flip_time & 1)) or \
            (S[i] == P[i] and flip_time & 1):
            if (i + 1) & 1:
                return "No"
            else:
                if cs[i][0] != cs[i][1]:
                    return "No"

            flip_time += 1

    return "Yes"

T = int(input())
for _ in range(T):
    N = int(input())
    S, P = input(), input()
    ans = solve(N, S, P)
    print(ans)
