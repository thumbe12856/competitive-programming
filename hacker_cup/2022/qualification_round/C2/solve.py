from collections import Counter
from multiprocessing.connection import answer_challenge
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

can = [1, 2, 4, 8, 16, 32, 64, 128, 256]

def solve(N, C1):
  root = {}
  curr = root
  for c in C1:
    if c not in curr:
      curr[c] = {}
    curr = curr[c]
  curr['#'] = {}

  N2 = N << 1
  d = 0
  for i in range(1, len(can), 1):
    if can[i - 1] < N2 <= can[i]:
      d = i
      break

  ans = []
  def dfs(curr_d, curr):
    if len(ans) == N - 1:
      return

    if curr_d == d:
      ans.append(curr[:])
      return

    dfs(curr_d + 1, curr + '.')
    dfs(curr_d + 1, curr + '-')

  if C1[0] == '.':
    dfs(1, '-')
  else:
    dfs(1, '.')

  return ans

T = int(input())
for case_num in range(T):
    N = int(input())
    C1 = input().rstrip()
    ans = solve(N, C1)
    print("Case #{}:".format(case_num + 1))
    for a in ans:
      print(a)
