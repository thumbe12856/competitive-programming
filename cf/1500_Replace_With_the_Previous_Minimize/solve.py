import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, K, S):
    if K >= 25:
        return "a" * N

    dp = {}
    for i in range(26):
        dp[chr(ord("a") + i)] = chr(ord("a") + i)

    ans = ""
    for s in S:
        if K > 0 and s == dp[s]:
            min_c = chr(ord("z") + 1)
            for i in range(min(26, K + 1)):
                curr_c = chr(max(ord("a"), ord(s) - i))
                to = dp[curr_c]
                if min_c == chr(ord("z") + 1) or to < dp[min_c]:
                    min_c = curr_c

            diff = ord(s) - ord(min_c)
            target = dp[min_c]
            K -= diff
            for i in range(diff):
                dp[chr(ord(s) - i)] = target

        ans += dp[s]
    return ans

T = int(input())
for _ in range(T):
    N, K = get_ints()
    S = input().rstrip()
    print(solve(N, K, S))

