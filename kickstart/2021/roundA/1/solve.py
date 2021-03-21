
def solve(N, K, S):
    ans = float('inf')

    def cal(S):
        l, r = 0, N - 1
        cnt = 0
        while l < r:
            if S[l] != S[r]:
                cnt += 1
            l += 1
            r -= 1
        return cnt

    return abs (K - cal(S))

T = int(input())
for num_test_cases in range(T):
    N, K= map(int, input().split())
    S = list(input())
    ans = solve(N, K, S)
    print("Case #{}: {}".format(num_test_cases + 1, ans))
