def solve(N):
    def cal(mid):
        val = (1 + mid) * mid // 2
        if val > N + 1:
            return False
        return True

    l, r = 1, N + 1
    while l < r:
        mid = (l + r) // 2
        if cal(mid):
            l = mid + 1
        else:
            r = mid

    return N - (l - 1) + 1

N = int(input())
print(solve(N))
