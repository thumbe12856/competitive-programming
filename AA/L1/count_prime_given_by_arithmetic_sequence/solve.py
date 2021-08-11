LIMIT = 40000001
not_primes = [0] * LIMIT
not_primes[1] = 1
for i in range(2, LIMIT, 1):
    if not not_primes[i]:
        for j in range(i * 2, LIMIT, i):
            not_primes[j] = 1

def solve(A, D, N):
    ans = N
    curr = A
    idx = 0
    while idx < N:
        ans -= not_primes[curr]
        curr += D
        idx += 1
    return ans

A, D, N = map(int, input().split())
print(solve(A, D, N))
