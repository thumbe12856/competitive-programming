def solve(N):
    ans = 0
    while N > 1:
        if N & 1:
            N -= 1
            ans += 1
        else:
            if N == 2:
                return ans + 1
            return ans + 2

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
