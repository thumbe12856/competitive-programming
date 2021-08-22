import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, nums):
    ans = 0
    for j in range(1, N, 1):
        # nums[i] * nums[j] = i + 1 + j + 1
        ni = 1
        while True:
            i = ni * nums[j] - j - 2
            if i >= j:
                break
            elif 0 <= i < j:
                if nums[i] == ni:
                    ans += 1
            ni += 1

    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
