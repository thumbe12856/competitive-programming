from collections import Counter
from functools import lru_cache

def solve(N, K, S):
    max_cnt = Counter(S)["*"]
    if max_cnt <= 2:
        return max_cnt
    
    for i in range(N):
        if S[i] == "*":
            S[i] = "x"
            break
    for i in range(N - 1, -1, -1):
        if S[i] == "*":
            S[i] = "x"
            break

    @lru_cache(None)
    def dfs(last_idx, idx):
        if idx >= N:
            return 0

        if S[idx] == ".":
            return dfs(last_idx, idx + 1)

        elif S[idx] == "x":
            if idx - last_idx > K:
                return float('inf')
            return dfs(idx, idx + 1)

        else: # .
            if idx - last_idx > K:
                return float('inf')

            return min(1 + dfs(idx, idx + 1), dfs(last_idx, idx + 1))

    val = dfs(float('inf'), 0)
    return 2 + val

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = list(input())
    print(solve(N, K, S))

