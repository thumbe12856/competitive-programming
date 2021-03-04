from functools import lru_cache

T = int(input())
for _ in range(T):
    N, lucky = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    @lru_cache(None)
    def check(n):
        if str(lucky) in str(n):
            return True
        return False

    @lru_cache(None)
    def dfs(m, n):
        if m > n:
            return False
        elif check(m):
            return True
        return dfs(m + lucky, n)

    for n in nums:
        if n < lucky:
            print("No")
            continue

        m = n % lucky
        if dfs(m, n):
            print("Yes")
        else:
            print("No")
