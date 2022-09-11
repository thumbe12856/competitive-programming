from collections import Counter
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, K, nums):
  cn = Counter(nums)
  for n in cn:
    if cn[n] > 2:
      return "NO"

  if N > K * 2:
    return "NO"

  return "YES"

T = int(input())
for case_num in range(T):
    N, K = get_ints()
    nums = get_ints()
    ans = solve(N, K, nums)
    print("Case #{}: {}".format(case_num + 1, ans))
