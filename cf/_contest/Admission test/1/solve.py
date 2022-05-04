import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N = int(input())
nums = get_ints()
can = {
    (float('-inf'), float('-inf')): 0
}
for i in range(N):
    next_can = {}
    for a, b in can:
        if nums[i] >= max(a, b):
            key = max(a, b, nums[i]), min(a, b)
            next_can[key] = max(next_can.get(key, float('-inf')), can[a, b] + nums[i])
        elif max(a, b) > nums[i] >= min(a, b):
            key = max(a, b), max(nums[i], min(a, b))
            next_can[key] = max(next_can.get(key, float('-inf')), can[a, b] + nums[i])

    for key in next_can:
        can[key] = max(next_can[key], can.get(key, float('-inf')))

ans = 0
for key in can:
    ans = max(ans, can[key])
print(ans)
