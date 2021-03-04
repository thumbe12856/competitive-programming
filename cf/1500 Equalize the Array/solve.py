from collections import Counter, defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    cn = Counter(nums)
    times = defaultdict(int)
    for c in cn:
        times[cn[c]] += 1

    st = list(sorted(times.keys()))
    presum = [0]
    for t in st:
        presum.append(presum[-1] + t * times[t])

    # print(times)
    # print(st)
    # print(presum)

    last_val = st[-1]
    last = 0
    cnt = 0
    ans = N
    for i in range(len(st) - 1, -1, -1):
        ans = min(
            ans,
            presum[i] + last + (last_val - st[i]) * cnt
        )
        # print(ans, presum[i], last_val, st[i], cnt)
        last += (last_val - st[i]) * cnt
        cnt += times[st[i]]
        last_val = st[i]
    print(ans)
