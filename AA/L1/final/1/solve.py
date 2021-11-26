import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N):
    if N == 1:
        return 2
    elif N == 2:
        return 3

    ans = 2
    cnt = 2
    while cnt <= N:
        ans += 1
        cnt += cnt // 2
    return ans

N = int(input())
print(solve(N))
