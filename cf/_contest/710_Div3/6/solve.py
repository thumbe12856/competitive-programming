import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, R, C):
    ans = 0
    sorted_idx = sorted(
        range(N),
        key=lambda i: (R[i], C[i])
    )

    r, c = 1, 1
    for i in sorted_idx:
        diff = r - c
        next_r, next_c = R[i], C[i]
        next_diff = next_r - next_c

        if r == next_r and c == next_c:
            continue

        if diff == next_diff and not (r + c) & 1: # even
            ans += next_c - c

        elif diff // 2 != next_diff // 2:
            ans += abs(diff // 2 - next_diff // 2)

        r, c = next_r, next_c

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    R = get_ints()
    C = get_ints()
    ans = solve(N, R, C)
    print(ans)
