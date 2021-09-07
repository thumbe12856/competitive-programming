import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    cnt = 1
    vis = {}
    ans = [0] * N
    for idx in sorted(range(N), key=lambda i: nums[i]):
        if nums[idx] not in vis:
            vis[nums[idx]] = cnt
            cnt += 1
        ans[idx] = vis[nums[idx]]

    print(*ans)

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()

    import random
    N = 10 ** 6
    nums = [random.randint(1, 2 * 10 ** 6 + 1) for _ in range(N)]

    import time
    s = time.time()
    solve(N, nums)
    e = time.time()
    print(e - s)
