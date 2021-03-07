def solve(S):
    if "m" in S or "w" in S:
        return 0

    N = len(S)
    last_val = 1
    last_last_val = 1
    for i in range(N - 2, -1, -1):
        curr_val = last_val
        if i + 1 < N:
            if S[i] == "u" and S[i + 1] == "u":
                curr_val += last_last_val

            elif S[i] == "n" and S[i + 1] == "n":
                curr_val += last_last_val

        last_last_val = last_val
        last_val = curr_val

    return last_val % (10 ** 9 + 7)

S = input()
print(solve(S))
