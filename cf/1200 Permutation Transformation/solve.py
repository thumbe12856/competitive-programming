T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    def dfs(ans, nums, d, s):
        if not nums:
            return

        max_val = max(nums)
        max_idx = nums.index(max_val)
        ans[s + max_idx] = str(d)
        dfs(ans, nums[:max_idx], d + 1, s)
        dfs(ans, nums[max_idx + 1:], d + 1, s + max_idx + 1)

    ans = [''] * N
    dfs(ans, nums, 0, 0)
    # print(ans)
    print((' ').join(ans))
