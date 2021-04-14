def solve(P, Q):
    can = []
    q = Q
    i = 2
    while i ** 2 <= q:
        if q % i == 0:
            can.append(i)
            while q % i == 0:
                q //= i
        i += 1

    if q > 1:
        can.append(q)

    ans = 0
    for c in can:
        p = P
        while p % Q == 0:
            p //= c
        ans = max(ans, p)

    return ans

T = int(input())
for _ in range(T):
    P, Q = map(int, input().split())
    print(solve(P, Q))
