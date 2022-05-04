MOD = 10 ** 9 + 7

def trans(S, K):
    k = 1
    res = 0
    for i in range(len(S) - 1, -1, -1):
        res += k * (ord(S[i]) - ord("a") + 1)
        k = (k * K) % MOD
    return res

def solve(S, N, K):
    ans = 0
    length = (N + 1) // 2
    pattern = ""
    for i in range(length):
        pattern += S[i]
    upper = trans(pattern, K)
    lower = trans("a" * length, K)
    ans = upper - lower + 1

    j = N // 2
    valid = True
    for i in range(len(pattern) - 1, -1, -1):
        if pattern[i] > S[j]:
            ans -= 1
            valid = False
            break
        elif pattern[i] < S[j]:
            valid = False
            break
        j += 1

    if valid:
        ans -= 1

    return ans % MOD


T = int(input())
for case_num in range(T):
    N, K = map(int, input().split())
    S = input()
    ans = solve(S, N, K)
    print("Case #{}: {}".format(case_num + 1, ans))

