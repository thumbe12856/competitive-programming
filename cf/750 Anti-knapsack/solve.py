T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    ans = []
    for i in range((K + 1) // 2, K):
        ans.append(str(i))

    for i in range(K + 1, N + 1, 1):
        ans.append(str(i))

    print(len(ans))
    if ans:
        print((" ").join(ans))

