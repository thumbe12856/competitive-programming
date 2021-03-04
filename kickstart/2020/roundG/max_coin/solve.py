def solve(mat):
    ans = 0
    for i in range(len(mat) - 1, -1, -1):
        x, y = i, 0
        temp = 0
        while x < N and y < N:
            temp += mat[x][y]
            x += 1
            y += 1

        ans = max(ans, temp)

    for i in range(len(mat)):
        x, y = 0, i
        temp = 0
        while x < N and y < N:
            temp += mat[x][y]
            x += 1
            y += 1

        ans = max(ans, temp)
    return ans

T = int(input())
for t in range(T):

    N = int(input())
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))

    ans = solve(mat)
    print("Case #{}: {}".format(t + 1, ans))
