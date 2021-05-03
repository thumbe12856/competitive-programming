def cal(L, R, curr):
    total = 0

    # N ^ 2 + (curr - 1) * N
    l, r = 1, L
    target = L
    idx = 0
    while l < r:
        mid = (l + r) // 2
        val = mid * mid + (curr - 1) * mid
        if val <= target:
            l = mid + 1
            idx = mid
        else:
            r = mid

    val = idx * idx + (curr - 1) * idx
    total += idx
    if L >= val:
        L -= val

    # N ^ 2 + curr * N
    l, r = 1, R
    target = R
    idx = 0
    while l < r:
        mid = (l + r) // 2
        val = mid * mid + curr * mid
        if val <= target:
            idx = mid
            l = mid + 1
        else:
            r = mid
    val = idx * idx + curr * idx
    total += idx
    if R >= val:
        R -= val

    return L, R, total

def solve(L, R):
    diff = L - R
    target = abs(diff) * 2
    curr = 1
    l, r = 1, target
    while l < r:
        mid = (l + r) // 2
        val = mid * (mid + 1)
        if val < target:
            l = mid + 1
            curr = mid + 1
        elif val == target:
            l = mid
            curr = mid + 1
            break
        else:
            r = mid
            curr = mid

    while curr * (curr + 1) <= target:
        curr += 1

    if curr > 1:
        prev = (curr - 1) * curr // 2
        if diff < 0:
            R -= prev
        else:
            L -= prev
    else:
        if L >= R and L >= 1:
            L -= 1
            curr += 1
        elif R > L and R >= 1:
            R -= 1
            curr += 1

    if L >= R:
        L, R, total = cal(L, R, curr)
        ans = total + curr - 1
    else:
        R, L, total = cal(R, L, curr)
        ans = total + curr - 1

    return "{} {} {}".format(ans, L, R)

T = int(input())
for case_num in range(T):
    L, R = map(int, input().split())

    ans = solve(L, R)
    print("Case #{}: {}".format(case_num + 1, ans))
