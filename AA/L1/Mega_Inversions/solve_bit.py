import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
        self.n = n
        self.total = 0

    def update(self, idx, val=1):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & (-idx)
        self.total += val

    def get(self, idx):
        if idx >= self.n:
            return self.total
        res = 0
        while idx:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

def solve(N, nums):
    max_val = max(nums)
    l_tree = BIT(max_val) # how many val bigger than x
    r_tree = BIT(max_val) # how many val smaller than x
    for n in nums:
        r_tree.update(n)

    ans = 0
    for i in range(N):
        n = nums[i]
        r_tree.update(n, -1)
        l_tree.update(n)

        l, r = i + 1 - l_tree.get(n), r_tree.get(n - 1)
        ans += l * r
    return ans

N = int(input())
nums = get_ints()
print(solve(N, nums))
