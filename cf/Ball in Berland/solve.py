from collections import defaultdict

T = int(input())
for _ in range(T):
    a, b, N = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_map, B_map = defaultdict(set), defaultdict(set)
    sa, sb = 0, 0
    for i in range(N):
        A_map[A[i]].add(B[i])
        B_map[B[i]].add(A[i])

    ans = 0
    for a in A_map:
        for b in A_map[a]:
            ans += N - (len(A_map[a]) + len(B_map[b])) + 1

    print(ans // 2)
