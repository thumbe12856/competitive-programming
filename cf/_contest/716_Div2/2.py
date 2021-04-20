MOD = 10 ** 9 + 7

def solve(N, K):
    if N == 1:
        return 1
    ans = (N ** K)
    return ans % MOD

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))
