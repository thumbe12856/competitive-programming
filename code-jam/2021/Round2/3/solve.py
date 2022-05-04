from collections import defaultdict, deque
from functools import lru_cache
from heapq import *
from itertools import product, permutations
import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

MOD = 10 ** 9 + 7
def solve(N, nums):
    dp = [
        [i, i, [j for j in range(N) if j != i]] for i in range(N)
    ]

    print(dp)
    for i in range(1, N):
        next_dp = []
        if nums[i] > nums[i - 1]:
            for curr_min, curr_max, arr in dp:
                for j in range(len(arr)):
                    if arr[j] < curr_min:
                        next_dp.append(
                            [arr[j], curr_max, arr[:j] + arr[j + 1:]]
                        )
                    else:
                        break
        else:
            for curr_min, curr_max, arr in dp:
                for j in range(len(arr) - 1, -1, -1):
                    if arr[j] > curr_max:
                        next_dp.append(
                            [arr[j], arr[j], arr[:j] + arr[j + 1:]]
                        )
                    else:
                        break


        print(next_dp)
        dp = next_dp

    return len(dp) % MOD


def solve2(N, nums):
    ans = 0
    order = [i for i in range(N)]
    for can in permutations(order):
        continue

        valid = True
        stack = []
        for i in range(N):
            while stack and stack[-1] < can[i]:
                stack.pop()
            stack.append(can[i])

            if nums[i] != len(stack):
                valid = False
                break

        if valid:
            ans += 1

    return ans % MOD

T = int(input())
for case_num in range(T):
    N = int(input())
    nums = get_ints()

    # if N > 13:
    #     sys.exit()

    ans = solve2(N, nums)
    print("Case #{}: {}".format(case_num + 1, ans))
