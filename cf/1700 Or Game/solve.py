import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, K, X, A):
    prefix, suffix = [0] * (N + 1), [0] * (N + 1)
    for i in range(N):
        prefix[i] = prefix[i - 1] | A[i]

    for i in range(N - 1, -1, -1):
        suffix[i] = suffix[i + 1] | A[i]

    ans = 0
    val = X ** K
    for i in range(N):
        ans = max(
            ans,
            prefix[i - 1] | A[i] * val | suffix[i + 1]
        )

    return ans

N, K, X = map(int, input().split())
A = get_ints()
print(solve(N, K, X, A))
