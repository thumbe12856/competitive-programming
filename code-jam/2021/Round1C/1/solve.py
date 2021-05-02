import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, K, nums):
    last = -1
    can = []
    for i in nums:
        if last == -1:
            can.append(i - 1)
        else:
            l, r = last + 1, i - 1
            can.append((r - l + 1 + 1) // 2)

        last = i

    if last != -1:
        can.append(K - last)

    can.sort()
    ans = 0
    cnt = 2
    while can and cnt:
        ans += can.pop()
        cnt -= 1
    return ans / K

def solve2(N, K, nums):
    last = -1
    ans = 0
    for i in nums:
        if last == -1:
            ans = max(ans, i - 1)
        else:
            l, r = last + 1, i - 1
            ans = max(ans, r - l + 1)

        last = i
    return ans / K

T = int(input())
for case_num in range(T):
    N, K = get_ints()
    nums = get_ints()
    nums.sort()
    ans = max(solve(N, K, nums), solve2(N, K, nums))
    print("Case #{}: {}".format(case_num + 1, ans))
