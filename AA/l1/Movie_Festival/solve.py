import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, q):
    q.sort()
    last = -1
    ans = 0
    for out_t, in_t in q:
        if in_t >= last:
            ans += 1
            last = out_t

    return ans

N = int(input())
q = []
for _ in range(N):
    a, b = get_ints()
    q.append((b, a))

print(solve(N, q))
