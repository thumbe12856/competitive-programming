T = int(input())

def solve(N, nums):
    ans = 0
    for i in range(1, N, 1):
        if nums[i] <= nums[i - 1]:
            next_n = nums[i]
            s1 = str(nums[i - 1])
            s2 = str(nums[i])
            diff = len(s1) - len(s2)
            if diff == 0:
                next_n = nums[i] * 10
                ans += 1

            else:
                type = 0
                for j in range(min(len(s1), len(s2))):
                    if s2[j] < s1[j]:
                        type = 1
                        break
                    elif s2[j] > s1[j]:
                        type = 2
                        break

                if type == 1:
                    next_n = nums[i] * (10 ** (diff + 1))
                    ans += diff + 1

                elif type == 2:
                    next_n = nums[i] * (10 ** diff)
                    ans += diff

                else:
                    target = nums[i - 1] + 1
                    st = str(target)
                    valid = True
                    for j in range(min(len(st), len(s1), len(s2))):
                        if st[j] != s2[j]:
                            valid = False

                    if valid:
                        next_n = nums[i - 1] + 1
                        ans += diff
                    else:
                        next_n = nums[i] * (10 ** (diff + 1))
                        ans += diff + 1

            nums[i] = next_n
    return ans

for case_num in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = solve(N, nums)
    print("Case #{}: {}".format(case_num + 1, ans))
