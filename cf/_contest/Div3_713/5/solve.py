def solve(N, L, R, S):
    n = N
    max_val, min_val = 0, (1 + R - L + 1) * (R - L + 1) // 2
    for _ in range(R - L + 1):
        max_val += n
        n -= 1

    if not (min_val <= S <= max_val):
        return -1

    diff = max_val - S
    can = []
    for i in range(R - L + 1):
        can += [N - i]
    can.reverse()

    idx = 0
    while diff:
        curr = min(diff, can[idx] - (idx + 1))
        can[idx] -= curr
        diff -= curr
        idx += 1

    ans = []
    idx = 0
    all_can = set([i + 1 for i in range(N)])
    for c in can:
        all_can.remove(c)

    for i in range(1, N + 1, 1):
        if i < L or i > R:
            ans += [str(all_can.pop())]
        else:
            ans += [str(can[idx])]
            idx += 1
    return (" ").join(ans)

T = int(input())
for _ in range(T):
    N, L, R, S = map(int, input().split())
    print(solve(N, L, R, S))
