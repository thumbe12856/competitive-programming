def solve(N, K):
    if not (0 <= K <= (N - 1) // 2):
        return -1

    ans = [0] * N
    can = [i + 1 for i in range(N)]
    for i in range(K):
        val = can.pop()
        ans[i * 2 + 1] = val

    for i in range(N):
        if ans[i] == 0:
            ans[i] = can.pop()

    return (" ").join(map(str, ans))

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))
