def solve(N, A, B, C, L):
    def dfs(idx, a, b, c):
        if idx == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            return float('inf')

        return min(
            dfs(idx + 1, a, b, c),
            10 + dfs(idx + 1, a + L[idx], b, c),
            10 + dfs(idx + 1, a, b + L[idx], c),
            10 + dfs(idx + 1, a, b, c + L[idx]),
        )

    return dfs(0, 0, 0, 0)


N, A, B, C = map(int, input().split())
L = []
for _ in range(N):
    L.append(int(input()))

print(solve(N, A, B, C, L))
