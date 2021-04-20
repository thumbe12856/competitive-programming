T = int(input())
for _ in range(T):
    N = int(input())
    G = []
    for i in range(N):
        G.append(list(input()))

    can = []
    X, Y = set(), set()
    for i in range(N):
        for j in range(N):
            if G[i][j] == "*":
                can.append((i, j))
                X.add(i)
                Y.add(j)

    if len(X) == 2 and len(Y) == 2:
        G[min(X)][max(Y)] = "*"
        G[max(X)][min(Y)] = "*"
        G[min(X)][min(Y)] = "*"
        G[max(X)][max(Y)] = "*"

    elif len(X) == 1:
        for next_x in range(N):
            if next_x not in X:
                G[next_x][max(Y)] = "*"
                G[next_x][min(Y)] = "*"
                break
    else:
        for next_y in range(N):
            if next_y not in Y:
                G[min(X)][next_y] = "*"
                G[max(X)][next_y] = "*"
                break

    for i in range(N):
        print(("").join(G[i]))
