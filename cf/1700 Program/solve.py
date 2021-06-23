import sys
input = sys.stdin.readline

def build(N, S):
    vals = [0]
    left = [(0, 0)]
    curr = 0
    curr_max, curr_min = 0, 0
    for i in range(N):
        if S[i] == "+":
            curr += 1
        else:
            curr -= 1
        curr_max = max(curr_max, curr)
        curr_min = min(curr_min, curr)
        left.append((curr_min, curr_max))
        vals.append(curr)

    right = [(0, 0) for _ in range(N + 1)]
    curr_max, curr_min = 0, 0
    for i in range(N - 1, -1, -1):
        if S[i] == "+":
            c = 1
        else:
            c = -1

        curr_max = max(0, curr_max + c)
        curr_min = min(0, curr_min + c)
        right[i] = (curr_min, curr_max)

    return left, right, vals

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    S = input()

    left, right, vals = build(N, S)
    for i in range(M):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        val = (
            max(left[l][1], right[r + 1][1] + vals[l]) -
            min(left[l][0], right[r + 1][0] + vals[l])
        ) + 1
        print(val)
