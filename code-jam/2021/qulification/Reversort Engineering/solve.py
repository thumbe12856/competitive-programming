def solve(N, C):
    min_val = N - 1
    max_val = min_val + (1 + N - 1) * (N - 1) // 2

    if not (min_val <= C <= max_val):
        return "IMPOSSIBLE"

    S = [str(i) for i in range(1, N + 1, 1)]
    l, r = 0, N - 1
    turn = 0
    curr = min_val
    while curr != C:
        curr_max = curr + r - l
        if curr_max <= C:
            S[l: r + 1] = reversed(S[l: r + 1])
            if turn == 0:
                r -= 1
            else:
                l += 1
            curr = curr_max
        else:
            diff = C - curr
            S[l: l + diff + 1] = reversed(S[l: l + diff + 1])
            curr = C
        turn = 1 - turn
    return (" ").join(S)

T = int(input())
for test_num in range(T):
    N, C = map(int, input().split())
    ans = solve(N, C)
    print("Case #{}: {}".format(test_num + 1, ans))
