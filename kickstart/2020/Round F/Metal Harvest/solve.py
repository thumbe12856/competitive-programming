import math

def solve(N, K, intervals):
    ans = 0
    intervals = sorted(intervals)
    last_start, last_end = intervals[0]
    need_pad = (last_end - last_start) % K > 0
    pad = 0
    if need_pad:
        pad = K
    last_end = last_start + (last_end - last_start) // K * K + pad

    for i in range(1, N):
        s, e = intervals[i]
        if s <= last_end:
            if last_end >= e:
                continue

            need_pad = (e - last_start) % K > 0
            pad = 0
            if need_pad:
                pad = K
            last_end = last_start + (e - last_start) // K * K + pad
        else:
            diff = last_end - last_start
            ans += math.ceil(diff / K)

            last_start = s
            last_end = e
            need_pad = (last_end - last_start) % K > 0
            pad = 0
            if need_pad:
                pad = K
            last_end = last_start + (last_end - last_start) // K * K + pad

    diff = last_end - last_start
    ans += math.ceil(diff / K)
    return ans

T = int(input())
for sample_num in range(T):
    N, K = list(map(int, input("").split()))
    intervals = set()
    for i in range(N):
        s, t = list(map(int, input("").split()))
        intervals.add((s, t))

    ans = solve(N, K, intervals)
    print("Case #{0}: {1}".format(sample_num + 1, ans))
