import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

LIMIT = 10000010
can = [0] * LIMIT
for i in range(1, LIMIT, 1):
    if can[i] != 0:
        continue

    j = 1
    while i * j * j < LIMIT:
        can[i * j * j] = i
        j += 1

def solve(N, nums):
    ans = 1
    vis = set()
    for n in nums:
        if can[n] in vis:
            vis = set()
            ans += 1
        vis.add(can[n])

    return ans

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    nums = get_ints()
    print(solve(N, nums))
