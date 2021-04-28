import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

def solve(f, t):
    if f > t:
        return "No"

    cnt1, cnt2 = 0, 0
    while f or t:
        if f & 1:
            cnt1 += 1

        if t & 1:
            cnt2 += 1

        f >>= 1
        t >>= 1

        if cnt1 < cnt2:
            return "No"

    return "Yes"

T = int(input())
for _ in range(T):
    f, t = get_ints()
    print(solve(f, t))
