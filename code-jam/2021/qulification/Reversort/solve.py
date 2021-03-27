T = int(input())

def solve(N, nums):
    ans = 0
    for i in range(N - 1):
        min_val, min_idx = nums[i], i
        for j in range(i + 1, N):
            if nums[j] < min_val:
                min_val = nums[j]
                min_idx = j

        nums[i: min_idx + 1] = reversed(nums[i: min_idx + 1])
        ans += min_idx - i + 1

    return ans

for test_num in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = solve(N, nums)
    print("Case #{}: {}".format(test_num + 1, ans))
