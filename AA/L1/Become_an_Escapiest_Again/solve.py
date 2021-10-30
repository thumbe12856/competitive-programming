import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, G):
    q = set([(0, 0, 1, 1), (0, 0, 1, -1)])
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    vis = set()
    while q:
        next_q = set()
        for i, j, d, f in q:
            if i == N - 1 and j == N - 1:
                return d

            key = (i, j, f)
            if key in vis:
                continue

            curr_val = G[i][j]
            vis.add(key)
            for x, y in dirs:
                if 0 <= i + x < N and 0 <= j + y < N:
                    next_val = G[i + x][j + y]
                    valid = False

                    # inc
                    if f == 1 and next_val > curr_val:
                        valid = True

                    # dec
                    elif f == -1 and next_val < curr_val:
                        valid = True

                    next_key = (i + x, j + y, d + 1, -f)
                    if valid and next_key not in vis:
                        next_q.add(next_key)

        q = next_q

    return -1

N = int(input())
G = []
for _ in range(N):
    G.append(get_ints())

print(solve(N, G))
