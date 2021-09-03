import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(q):
    q.sort()
    ans = 0
    last_start, last_end = -1, -1
    for s, e in q:
        if s < last_end and last_start < e:
            last_start = max(last_start, s)
            last_end = min(last_end, e)
        else:
            last_start, last_end = s, e
            ans += 1

    return ans

N, Q = map(int, input().split())
q = []
for _ in range(Q):
    a, b = get_ints()
    q.append((a, b))

print(solve(q))
