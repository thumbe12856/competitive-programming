# https://cses.fi/problemset/task/1630/

def solve(N, q):
    q.sort()
    ans, t = 0, 0
    for i in range(N):
        t += q[i][0]
        ans += q[i][1] - t
    return ans

q = []
N = int(input())
for _ in range(N):
    a, d = map(int, input().split())
    q.append((a, d))

print(solve(N, q))
