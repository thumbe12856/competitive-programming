import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):

T = int(input())
for case_num in range(T):
    print("Case #{}: {}".format(case_num + 1, ans))
