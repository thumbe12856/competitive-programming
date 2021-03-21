def solve(N, G):
    can = []
    max_total = N

    def dfs(node, parent):
        nonlocal can, max_total

        total = 1
        res = 0
        for next_node in G[node]:
            if next_node == parent:
                continue

            ret = dfs(next_node, node)
            res = max(res, ret)
            total += ret

        res = max(res, N - total)
        if res < max_total:
            max_total = res
            can = [node]
        elif res == max_total:
            can.append(node)

        return total

    dfs(1, 0)
    if len(can) == 1:
        target = G[1].pop()
        print(1, target)
        print(1, target)
    else:
        v1, v2 = can[0], can[1]
        for n in G[v1]:
            if n == v2:
                continue
            target = n
            break
        print(v1, target)
        print(v2, target)

T = int(input())
for _ in range(T):
    N = int(input())
    G = [[] for i in range(N + 1)]
    for _ in range(N - 1):
        f, t = list(map(int, input().split()))
        G[f].append(t)
        G[t].append(f)

    solve(N, G)
