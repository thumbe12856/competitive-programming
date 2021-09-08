from collections import Counter
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, nums):
    for i in range(1, N, 1):
        nums[i] -= i + nums[0]
    nums[0] = 0
    cn = Counter(nums)
    ans = 0
    for c in cn:
        if cn[c] > 1:
            print(cn[c], (1 + cn[c] - 1) * (cn[c] - 1) // 2)
            if cn[c] == 2:
                ans += 1
            else:
                ans += (1 + cn[c] - 1) * (cn[c] - 1) // 2
    return ans * 2

N = int(input())
nums = get_ints()
print(solve(N, nums[:]) + solve(N, nums[::-1]))
