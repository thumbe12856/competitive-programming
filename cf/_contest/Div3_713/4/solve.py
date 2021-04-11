from collections import Counter, defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(target_N, nums):
    vis = Counter(nums)
    max_val, sec_max = -1, -1
    nums.sort()
    max_val, sec_max = nums[-1], nums[-2]
    total = sum(nums)

    vis[max_val] -= 1
    temp_total = total - max_val
    target = temp_total - max_val
    if target in vis and vis[target] > 0:
        ans = []
        vis[target] -= 1
        for v in vis:
            if vis[v] > 0:
                ans += [str(v)] * vis[v]
        return (" ").join(ans)
    vis[max_val] += 1

    vis[sec_max] -= 1
    temp_total = total - sec_max
    target = temp_total - sec_max
    if target in vis and vis[target] > 0:
        ans = []
        vis[target] -= 1
        for v in vis:
            if vis[v] > 0:
                ans += [str(v)] * vis[v]
        return (" ").join(ans)

    return -1

T = int(input())
for _ in range(T):
    target_N = int(input())
    nums = get_ints()
    print(solve(target_N, nums))
