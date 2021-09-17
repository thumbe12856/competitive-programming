import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, M, nums, Q):
    presum = [0]
    for n in nums:
        presum.append(presum[-1] + n)

    def find(l, target):
        r = len(presum) - 1
        while l < r:
            mid = l + (r - l) // 2
            if presum[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l

    curr = 0
    for q in Q:
        if presum[-1] - presum[curr] < q:
            q -= presum[-1] - presum[curr]
            curr = 0

        curr = find(curr, presum[curr] + q)

    return curr % N

N, M = get_ints()
nums = get_ints()
Q = get_ints()
print(solve(N, M, nums, Q))
