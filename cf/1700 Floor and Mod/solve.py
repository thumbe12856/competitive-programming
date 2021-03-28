def solve(x, y):
    ans = 0
    for i in range(2, y + 1, 1):
        j = i + 1
        k = 1
        while j <= min(i * i, x):
            k += 1
            j = (i + 1) * k
            ans += 1
    return ans

T = int(input())
while T:
    T -= 1
    x, y = map(int, input().split())
    ans = solve(x, y)
    print(ans)
