from collections import *

ans = 0
vis = defaultdict(int)
N = int(input())
for _ in range(N):
    S = input()
    cs = Counter(S)
    key = ""
    for i in range(26):
        key += str(cs[chr(ord("a") + i)]) + "_"
    vis[key] += 1

for v in vis:
    ans += (1 + vis[v] - 1) * (vis[v] - 1) // 2

print(ans)
