import sys

def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve2(N):
    if N <= 11:
        return 12
    S = str(N)

    length = len(S)
    ans = float('inf')
    sn = str(N)
    for i in range(1, length // 2 + 1, 1):
        curr = int(sn[:i])
        ans = min(ans, get_val(curr, N))

        curr = int(sn[:i]) + 1
        ans = min(ans, get_val(curr, N))

        for j in range(i - 1, i + 3, 1):
            curr = 10 ** j
            ans = min(ans, get_val(curr, N))

        # Reverse
        for j in range(i - 1, i + 3, 1):
            for k in range(20):
                curr = 10 ** j + k
                last_number = curr
                curr_s = str(curr)
                cnt = 0
                while int(curr_s) < N:
                    curr -= 1
                    if curr < 0:
                        break
                    cnt += 1
                    curr_s = str(curr) + curr_s

                if int(curr_s) > N and cnt > 0:
                    ans = min(ans, int(curr_s))

                s = curr_s[:-len(str(last_number))]
                if s:
                    cnt -= 1
                    val = int(s)
                    if val > N and cnt > 0:
                        ans = min(ans, val)

    return ans

T = int(input())
for case_num in range(T):
    N = int(input())
    ans = solve2(N)
    print("Case #{}: {}".format(case_num + 1, ans))
