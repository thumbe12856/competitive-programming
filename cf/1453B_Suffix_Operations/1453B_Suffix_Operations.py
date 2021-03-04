T = int(input(''))

for _ in range(T):
    N = int(input(''))
    nums = list(map(int, input('').split()))
    ans = float('inf')
    for idx in [0, 1]:
        max_diff = float('-inf')
        target = nums[idx]
        temp_ans = 0
        last_diff = 0
        for i in range(N):
            if i == 1 - idx:
                continue

            diff = target - (nums[i] + last_diff)
            last_diff += diff
            temp_ans += abs(diff)
        ans = min(ans, temp_ans)
    print(ans)
