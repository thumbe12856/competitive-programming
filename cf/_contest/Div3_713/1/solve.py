from collections import Counter

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    cn = Counter(nums)
    for c in cn:
        if cn[c] == 1:
            target = c
            break
    for i in range(N):
        if nums[i] == target:
            print(i + 1)
            break

