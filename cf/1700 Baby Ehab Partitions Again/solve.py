import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N = int(input())
nums = get_ints()
s = sum(nums)
dp = [False] * (s + 1)
dp[0] = True

for a in nums:
    for b in range(s - a, -1, -1):
        if dp[b]:
            dp[a + b] = True

if s & 1 or not dp[s // 2]:
    print(0)
else:
    res = -1
    norm = 30
    for i in range(N):
        n = nums[i]
        cnt = 0
        while not (n & 1):
            cnt += 1
            n >>= 1

        if cnt < norm:
            norm = cnt
            res = i

    print(1)
    print(res + 1)
