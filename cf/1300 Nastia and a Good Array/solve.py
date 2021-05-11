import sys
from math import gcd


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    steps = []
    for i in range(1, N, 1):
        if gcd(nums[i - 1], nums[i]) != 1:
            if nums[i - 1] <= nums[i]:
                nums[i] = nums[i - 1] + 1
                steps.append((i, i + 1, nums[i - 1], nums[i]))
            else:
                val = nums[i - 1] + 1
                if i - 2 >= 0:
                    while gcd(nums[i - 2], val) != 1 or gcd(val, nums[i]) != 1:
                        val += 1

                    nums[i - 1] = val
                    steps.append((i, i + 1, nums[i - 1], nums[i]))
                else:
                    nums[i - 1] = nums[i] + 1
                    steps.append((i, i + 1, nums[i - 1], nums[i]))

    print(len(steps))
    for i, j, x, y in steps:
        print(i, j, x, y)

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    solve(N, nums)
