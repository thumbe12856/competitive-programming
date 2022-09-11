from collections import Counter
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(M, N, G):
  if M == 1 or N == 1:
    for i in range(M):
      for j in range(N):
        if G[i][j] == '^':
          return False, None
    return True, G
  return True, ['^' * N for _ in range(M)]

T = int(input())
for case_num in range(T):
    M, N = get_ints()
    G = []
    for _ in range(M):
      G.append(input().rstrip())
    valid, res = solve(M, N, G)

    if not valid:
      print("Case #{}: Impossible".format(case_num + 1))
    else:
      print("Case #{}: Possible".format(case_num + 1))
      for r in res:
        print(r)
