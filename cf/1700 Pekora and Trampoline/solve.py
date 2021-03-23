def solve(N, nums):
    ans = 0
    for i in range(N):
        temp = 0
        for j in range(i):
            temp += max(0, nums[j] - (i - j))
        ans = max(ans, temp + nums[i] - 1)
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = solve(N, nums)
    print(ans)
