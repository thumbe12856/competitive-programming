T = int(input(""))

def solve():
    N = int(input(""))
    X, Y = [], []
    for _ in range(N):
        x, y = list(map(int, input("").split()))
        X.append(x)
        Y.append(y)

    Y.sort()
    target_y = Y[N // 2]
    ans = 0
    for y in Y:
        ans += abs(y - target_y)

    X.sort()
    for i in range(N):
        X[i] -= i
    X.sort()
    target_x = X[N // 2]
    for x in X:
        ans += abs(x - target_x)

    return ans

for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t + 1, ans))
