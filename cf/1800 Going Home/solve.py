from collections import Counter

def solve(N, nums):
    # Because 1 <= nums[i] <= 2.5 * 1e6,
    # the maximum value of the nums[i] + nums[j] will <= 5 * 1e6.
    # Therefore, O(N^2) => O(5 * 1e6), will never be TLE.

    res, ans = False, []
    vis = {}
    for i in range(N):
        for j in range(i):
            v = nums[i] + nums[j]
            if v in vis:
                ii, jj = vis[v]
                can = [i + 1, j + 1, ii + 1, jj + 1]
                if len(set(can)) == 4:
                    ans = can[:]
                    res = True
                    return res, ans
            else:
                vis[v] = (i, j)

    return False, []


N = int(input())
nums = list(map(int, input().split()))
res, ans = solve(N, nums)
if res:
    print("Yes")
    print(ans[0], ans[1], ans[2], ans[3])
else:
    print("No")

