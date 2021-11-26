import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, K, nums):
    ans = 0
    l, r = 0, N - 1
    while K:
        K -= 1
        l_val = nums[l] * nums[l + 1]
        r_val = nums[r] * nums[r - 1]
        if l_val < r_val:
            r -= 2
            ans += r_val
        else:
            l += 2
            ans += l_val

    return ans

N, K = get_ints()
nums = get_ints()
nums.sort()
print(solve(N, K, nums))
