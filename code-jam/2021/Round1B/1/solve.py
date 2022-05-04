import math
from itertools import permutations
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

M = 10 ** 9

def solve(A, B, C):
    if A == B == C:
        return "0 0 0 0"

    def check(h, m, s, ans_h, ans_m, ans_s):
        if s * M * 720 != ans_s:
            return False

        if (720 * m + 12 * s) * M != ans_m:
            return False

        if (3600 * h + (60 * m + s)) * M != ans_h:
            return False

        return True

    ans = ""
    q = [A, B, C]
    q.sort()
    q[1] -= q[0]
    q[2] -= q[0]
    q[0] = 0
    ret_s, ret_m, ret_h, ret_n = 0, 0, 0, 0
    valid = False
    for h, m, s in permutations(q):
        # nano_s = math.ceil(s / 720)
        # nano_m = math.ceil(m / 12)
        # nano_h = math.ceil(h / 1)
        # ret_h = math.floor(nano_h / (M * 3600))
        # ret_m = math.floor(nano_m / (M * 60))
        # ret_s = math.floor(nano_s / (M))

        print(ret_h, ret_s, ret_m, check(ret_h, ret_m, ret_s, h, m, s))
        # if check(ret_h, ret_m, ret_s, h, m, s):
        #     ret_n = s % 720
        #     valid = True
        #     break

    ans = "{} {} {} {}".format(ret_h, ret_m, ret_s, ret_n)
    return ans

T = int(input())
for case_num in range(T):
    A, B, C = get_ints()
    ans = solve(A, B, C)
    print("Case #{}: {}".format(case_num + 1, ans))
