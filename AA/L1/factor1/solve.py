from collections import defaultdict

def solve(X, Y):
    ans = 0
    cnt = defaultdict(lambda: 1)

    for i in range(2, Y + 1, 1):
        for j in range(i, Y + 1, i):
            cnt[j] += 1

    for i in range(X, Y + 1, 1):
        ans += cnt[i]

    return ans

X, Y = map(int, input().split())
print(solve(X, Y))
