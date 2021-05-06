import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, S):
    pos = []
    for i in range(N):
        if S[i] == "*":
            pos.append(i - len(pos))

    if len(pos) <= 1:
        return 0

    ans = 0
    length = len(pos)
    t_idx = length // 2
    for i in range(length):
        ans += abs(pos[t_idx] - pos[i])

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(solve(N, S))
