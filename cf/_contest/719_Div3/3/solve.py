from collections import defaultdict, deque
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve2(N):
    ans = [[0 for i in range(N)] for j in range(N)]
    can = [i + 1 for i in range(N ** 2)]
    turn = 0
    l, r = 0, len(can) - 1
    for i in range(N):
        for j in range(N):
            if turn == 0:
                ans[i][j] = can[l]
                l += 1
            else:
                ans[i][j] = can[r]
                r -= 1
            turn = 1 - turn

    ans[0][0], ans[-1][-1] = ans[-1][-1], ans[0][0]

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for i in range(N):
        for j in range(N):
            temp_can = set()
            for x, y in dirs:
                if 0 <= i + x < N and 0 <= j + y < N:
                    temp_can.add(ans[i + x][j + y])
            if ans[i][j] + 1 in temp_can or ans[i][j] - 1 in temp_can:
                print(-1)
                return

    for i in range(N):
        print((" ").join(map(str, ans[i])))


def solve(N):
    # can = [N ** 2 - i for i in range(N ** 2)]
    can = [i + 1 for i in range(N ** 2)]
    q = deque([(0, 0)])
    vis = [[float('inf') for i in range(N)] for j in range(N)]
    # vis = defaultdict(lambda: defaultdict(float('inf')))
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q and can:
        i, j = q.popleft()
        if vis[i][j] != float('inf'):
            continue
        temp_can = set()
        for x, y in dirs:
            if 0 <= i + x < N and 0 <= j + y < N:
                temp_can.add(vis[i + x][j + y])

        target_idx = None
        target = None
        print(i, j, temp_can)
        for ii in range(N):
            print((" ").join(map(str, vis[ii])))
        print()

        if len(can) == 3:
            for idx in range(len(can)):
                if can[idx] + 1 in temp_can or can[idx] - 1 in temp_can:
                    continue
                target = can[idx]
                target_idx = idx
                break

        else:
            for idx in range(len(can) - 1, -1, -1):
                if can[idx] + 1 in temp_can or can[idx] - 1 in temp_can:
                    continue
                target = can[idx]
                target_idx = idx
                break

        if target is None:
            print("J")
            print(-1)
            return

        val = can.pop(target_idx)
        vis[i][j] = val
        if 0 <= i + 1 < N and vis[i + 1][j] == float('inf'):
            q.append((i + 1, j))

        if 0 <= j + 1 < N and vis[i][j + 1] == float('inf'):
            q.append((i, j + 1))

    for i in range(N):
        for j in range(N):
            if vis[i][j] == float('inf'):
                print(-1)
                return

    for i in range(N):
        print((" ").join(map(str, vis[i])))

T = int(input())
for _ in range(T):
    N = int(input())
    solve2(N)
