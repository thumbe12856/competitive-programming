import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def d_sum(d):
    res = 0
    while d:
        res += d % 10
        d //= 10
    return res

def solve(L, R, V):
    l, r = L, L
    s = 0
    ans = 0
    while r <= R:
        s += d_sum(r)
        while s > V:
            s -= d_sum(l)
            l += 1
        ans += r - l + 1
        r += 1

    return ans

L, R, V1, V2 = get_ints()
print(solve(L, R, V2) - solve(L, R, V1 - 1))
