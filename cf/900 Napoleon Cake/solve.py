T = int(input())

def solve(N, nums):
    ans = [str(0)] * N
    q = []
    for i in range(N):
        if nums[i] != 0:
            q.append((max(0, i + 1 - nums[i]), i))

    q.sort()
    last_f, last_t = None, None
    for f, t in q:
        if last_f is None:
            last_f = f
            last_t = t
            continue

        if f <= last_t:
            last_t = max(last_t, t)
        else:
            for i in range(last_f, last_t + 1, 1):
                ans[i] = str(1)
            last_f = f
            last_t = t

    if last_f is not None:
        for i in range(last_f, last_t + 1, 1):
            ans[i] = str(1)
    return ans

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = solve(N, nums)
    print((" ").join(ans))
