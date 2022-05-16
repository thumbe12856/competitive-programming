def solve(S):
    N = len(S)
    o_idx = []
    for i in range(N):
        if S[i] == "1":
            o_idx.append(i)

    o_cnt = len(o_idx)
    z_cnt = N - o_cnt
    if not z_cnt or not o_cnt:
        return 0

    def check(n):
        # try to remove n "1"
        # check if the cost is smaller or equal than n

        x = len(o_idx) - n # left "1" number in the substring

        # substring = S[i: i + x]
        for i in range(n + 1):
            l = o_idx[i]
            r = o_idx[i + x - 1]

            # r - l + 1 = len(sub_string)
            # r - l + 1 - x = left "0" number in the sub_string
            if r - l + 1 - x <= n:
                return True
        return False

    ans = o_cnt
    l, r = 0, ans
    while l < r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            r = mid
        else:
            l = mid + 1

    return ans

T = int(input())
for _ in range(T):
    S = input().rstrip()
    print(solve(S))
