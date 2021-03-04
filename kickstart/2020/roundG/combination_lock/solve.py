def solve(nums, W, N):
    ans = float('inf')
    for i in range(1, N + 1, 1):
        temp_ans = 0
        valid = True
        for n in nums:
            if n > i:
                temp_ans += min(N - n + i, abs(i - n))
            else:
                temp_ans += min(N - i + n, abs(i - n))

            if temp_ans >= ans:
                valid = False
                break

        if valid:
            ans = min(ans, temp_ans)
    return ans

T = int(input())
for t in range(T):
    W, N = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ans = solve(nums, W, N)
    print("Case #{}: {}".format(t + 1, ans))
