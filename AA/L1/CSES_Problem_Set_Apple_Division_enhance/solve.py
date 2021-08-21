def solve(N, nums):
    s = sum(nums)

    def dfs(idx, curr):
        if idx == N:
            l = curr
            r = s - curr
            return abs(l - r)

        return min(
            dfs(idx + 1, curr),
            dfs(idx + 1, curr + nums[idx]),
        )

    return dfs(0, 0)

N = int(input())
nums = list(map(int, input().split()))
print(solve(N, nums))
