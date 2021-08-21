def solve(N, V, A):
    paths = []

    def dfs(idx, path, val):
        if idx == N:
            if val == V:
                paths.append(path)
            return

        for i in range(A[idx] + 1):
            dfs(idx + 1, path + [i], val ^ i)

    dfs(0, [], 0)
    print(len(paths))
    if paths:
        for p in paths:
            print("{}={}".format(
                ("^").join(map(str, p)),
                V
            ))

N, V = map(int, input().split())
A = list(map(int, input().split()))
solve(N, V, A)
