def solve(A, D, N):
    ans = 0
    target = A + N * D
    for n in range(A, target, D):
        ans += n + n - bin(n).count("1")
    return ans

A, D, N = map(int, input().split())
print(solve(A, D, N))
