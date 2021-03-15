import math

T = int(input(""))

def solve(N, X, nums):
    my_nums = []
    for i in range(N):
        v = math.ceil(nums[i] / X)
        my_nums.append((v, i))

    my_nums.sort()
    ans = [None] * N
    idx = 0
    for _, i in my_nums:
        ans[idx] = str(i + 1)
        idx += 1

    return ans

for _ in range(T):
    N, X = list(map(int, input("").split()))
    nums = list(map(int, input("").split()))
    ans = (" ").join(solve(N, X, nums))
    print("Case #{0}: {1}".format(_ + 1, ans))
