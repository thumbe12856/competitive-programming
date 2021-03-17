from math import ceil

test_cases = int(input())
for _ in range(test_cases):
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    T = list(map(int, input().split()))
    B[-1] = 0
    curr = 0

    for i in range(N):
        if i == N - 1:
            stay = 0
        else:
            stay = ceil((B[i] - A[i]) / 2)
        curr += A[i] - B[i - 1] + T[i] + stay
        curr = max(curr, B[i])

    print(curr)
