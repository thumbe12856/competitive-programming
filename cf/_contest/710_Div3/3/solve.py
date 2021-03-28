import random
from functools import lru_cache

def solve(A, B):

    @lru_cache(None)
    def dfs(s):
        if s in B:
            return len(B) - len(s)

        return 1 + min(dfs(s[:-1]), dfs(s[1:]))

    return dfs(A)

T = int(input())
for _ in range(T):
    A, B = input(), input()
    print(solve(A, B))
