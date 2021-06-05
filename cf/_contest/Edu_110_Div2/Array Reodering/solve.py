from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    p = defaultdict(set)
    even = []
    odd = []
    for i in range(N):
        if not(nums[i] & 1):
            even.append(nums[i])
            continue

        odd.append(nums[i])

        if nums[i] in p:
            continue

        j = 3
        n = nums[i]
        while j <= n:
            if n % j == 0:
                p[nums[i]].add(j)
                n //= j
            else:
                j += 2

    ans = 0
    for i in range(len(even)):
        ans += N - i - 1

    for i in range(len(odd)):
        for j in range(i + 1, len(odd), 1):
            if len(p[odd[i]].intersection(p[odd[j]])) >= 1:
                ans += 1

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
