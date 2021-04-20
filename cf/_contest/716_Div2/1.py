import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

can = set()
LIMIT = 10 ** 4
idx = 0
while idx <= LIMIT:
    can.add(idx ** 2)
    idx += 1

def solve(N, nums):
    for n in nums:
        if n not in can:
            return "Yes"

    return "No"

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
