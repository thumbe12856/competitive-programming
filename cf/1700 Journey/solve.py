import sys

def solve(N, dirs):
    ans = [1] * (N + 1)
    l_key, r_key = 0, 1
    vis = {}
    def move(ori_idx, ori_turn):
        l, r = ori_idx, ori_idx

        # Right
        idx = ori_idx
        turn = ori_turn
        while idx < N and (
            (turn == 0 and dirs[idx] == "R") or \
            (turn == 1 and dirs[idx] == "L")
        ):
            turn = 1 - turn
            idx += 1
            r = idx
            key = (turn, idx, r_key)
            if key in vis:
                r = vis[key]
                break

        turn = ori_turn
        for i in range(ori_idx, r + 1, 1):
            key = (turn, i, r_key)
            if key in vis:
                break

            turn = 1 - turn
            vis[key] = r

        # Left
        idx = ori_idx
        turn = ori_turn
        while idx > 0 and (
            (turn == 0 and dirs[idx - 1] == "L") or \
            (turn == 1 and dirs[idx - 1] == "R")
        ):
            turn = 1 - turn
            idx -= 1
            l = idx
            key = (turn, idx, l_key)
            if key in vis:
                l = vis[key]
                break

        turn = ori_turn
        for i in range(ori_idx, l - 1, -1):
            key = (turn, i, l_key)
            if key in vis:
                break

            turn = 1 - turn
            vis[key] = l

        return str(r - l + 1)

    for i in range(N + 1):
        ans[i] = move(i, 0)

    return (" ").join(ans)

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    dirs = input().rstrip()
    ans = solve(N, dirs)
    print(ans)
