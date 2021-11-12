import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, A, B):
    dp1 = [0] * (N + 1)
    dp2 = [0] * (N + 1)

    ans = 0
    for i in range(N):
        dp1[A[i]] = dp1[A[i] - 1] + 1
        dp2[B[i]] = dp2[B[i] - 1] + 1
        ans = max(
            ans,
            min(dp1[A[i]], dp2[A[i]]),
            min(dp1[B[i]], dp2[B[i]]),
        )

    return ans


N = int(input())
A = get_ints()
B = get_ints()
print(solve(N, A, B))
