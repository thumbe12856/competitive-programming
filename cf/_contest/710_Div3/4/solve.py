from collections import Counter, defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    ans = 0
    vis = defaultdict(int)
    max_cnt = 0
    for n in nums:
        vis[n] += 1
        max_cnt = max(max_cnt, vis[n])

    left = N - max_cnt
    if max_cnt > left:
        return max_cnt - left
    
    if N & 1:
        return 1
    return 0

T = int(input())
for i in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
