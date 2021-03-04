T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    nums = list(map(int, input().split()))
    P = list(map(int, input().split()))
    nums.sort(reverse=True)

    ans = 0
    idx = 0
    for i in range(len(nums)):
        if idx >= len(P) or P[nums[i] - 1] < P[idx]:
            ans += P[nums[i] - 1]
        else:
            ans += P[idx]
            idx += 1

    print(ans)
