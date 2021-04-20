import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    if N <= 3:
        return N

    left = [
        [2, float('inf')] for _ in range(N)
    ]
    left[0][0] = 1
    for i in range(1, N):
        diff = nums[i] - nums[i - 1]
        if diff == left[i - 1][1]:
            left[i][0] = left[i - 1][0] + 1
        left[i][1] = diff

    right = [
        [2, float('inf')] for _ in range(N)
    ]
    right[-1][0] = 1
    for i in range(N - 2, -1, -1):
        diff = nums[i + 1] - nums[i]
        if diff == right[i + 1][1]:
            right[i][0] = right[i + 1][0] + 1
        right[i][1] = diff

    ans = 0
    for i in range(N):
        ans = max(ans, left[i][0], right[i][0])
        if i > 0:
            ans = max(ans, left[i - 1][0] + 1) # 1, 2, 3, ?
        if i < N - 1:
            ans = max(ans, right[i + 1][0] + 1) # ?, 3, 2, 1

    for i in range(1, N - 1, 1):
        l, r = i - 1, i + 1
        l_diff, r_diff = left[l][1], right[r][1]
        val = (nums[l] + nums[r]) // 2
        curr_l_diff = val - nums[l]
        curr_r_diff = nums[r] - val
        if curr_l_diff == l_diff and curr_l_diff == curr_r_diff:
            ans = max(ans, left[l][0] + 2) # 1, 2, 3, ?, 5, 5
        if curr_r_diff == r_diff and curr_l_diff == curr_r_diff:
            ans = max(ans, right[r][0] + 2) # 5, 5, ?, 3, 2, 1

        if l_diff != r_diff and l_diff != float('inf') and r_diff != float('inf'):
            continue

        if curr_l_diff != curr_r_diff:
            continue
        elif curr_l_diff != l_diff and l_diff != float('inf'):
            continue
        elif curr_r_diff != r_diff and r_diff != float('inf'):
            continue

        ans = max(ans, left[l][0] + 1 + right[r][0]) # 6, 5, ?, 3, 2, 1

    return ans

T = int(input())
for case_num in range(T):
    N = int(input())
    nums = get_ints()
    ans = solve(N, nums)
    print("Case #{}: {}".format(case_num + 1, ans))
