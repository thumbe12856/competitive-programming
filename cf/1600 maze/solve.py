def solve(N, M, K, maze):
    ans = maze
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    x, y = None, None
    for i in range(M):
        for j in range(N):
            if maze[i][j] == ".":
                x, y = i, j
                break
        if x is not None:
            break

    vis = set()
    q = [(x, y)]
    traversal = []
    while q:
        i, j = q.pop()
        if (i, j) in vis:
            continue

        traversal.append((i, j))
        vis.add((i, j))
        for x, y in dirs:
            if not (0 <= i + x < M and 0 <= j + y < N):
                continue
            elif maze[i + x][j + y] != ".":
                continue
            q.append((i + x, j + y))

    while K:
        K -= 1
        i, j = traversal.pop()
        ans[i][j] = "X"
    return ans


M, N, K = map(int, input().split())
maze = []
for i in range(M):
    line = list(input())
    maze.append(line)

ans = solve(N, M, K, maze)
for i in range(M):
    print(("").join(ans[i]))
