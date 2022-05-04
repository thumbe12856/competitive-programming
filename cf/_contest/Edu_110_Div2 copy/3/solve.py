import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, S):
    l, r = 0, 0
    l_cnt, r_cnt = 0, 0
    for i in range(N):
        if S[i] == "(":
            if l_cnt:
                if r_cnt == 0:
                    l_cnt -= 1
                    l += 1
                else:
                    l_cnt += 1
            else:
                l_cnt += 1
        else:
            if r_cnt:
                l_cnt = 0
                r_cnt = 0
                l += 1
            else:
                if l_cnt == 1:
                    l_cnt = 0
                    r_cnt = 0
                    l += 1
                else:
                    r_cnt += 1
    return l, l_cnt + r_cnt

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    l, r = solve(N, S)
    print(l, r)
