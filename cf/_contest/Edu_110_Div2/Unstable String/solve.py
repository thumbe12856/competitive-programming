def solve(S):
    ans = 0
    N = len(S)
    left = 0
    last_c_idx = 0
    for i in range(N):
        c = S[i]
        if S[i] != "?" and S[last_c_idx] != "?":
            if (i - last_c_idx) & 1:
                target = str(1 - int(S[i]))
            else:
                target = S[i]

            if S[last_c_idx] != target:
                last_c_idx += 1
                left = last_c_idx

        ans += (i - left) + 1

        if c != "?":
            last_c_idx = i

    return ans

T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
