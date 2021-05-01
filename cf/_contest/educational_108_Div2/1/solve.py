import math
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(r, b, d):
    min_val = min(r, b)
    max_val = max(r, b)
    diff = max_val - min_val

    if math.ceil(diff / min_val) <= d:
        return "Yes"
    return "No"

T = int(input())
for _ in range(T):
    r, b, d = get_ints()
    print(solve(r, b, d))
