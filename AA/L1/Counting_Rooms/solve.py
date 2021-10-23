def dfs(G, i, j):
    M, N = len(G), len(G[0])
    if G[i][j] != ".":
        return

    G[i][j] = "#"
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for x, y in dirs:
        if not (0 <= i + x < M and 0 <= j + y < N):
            return

        dfs(G, i + x, j + y)

def solve(M, N, G):
    ans = 0
    for i in range(M):
        for j in range(N):
            if G[i][j] == ".":
                dfs(G, i, j)
                ans += 1
    return ans

M, N = map(int, input().split())
G = []
for _ in range(M):
    l = list(input().strip())
    G.append(l)

print(solve(M, N, G))
