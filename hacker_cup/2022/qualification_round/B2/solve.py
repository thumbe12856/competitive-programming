from collections import Counter
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def solve(M, N, G):
  if M == 1 or N == 1:
    for i in range(M):
      for j in range(N):
        if G[i][j] == '^':
          return False, None
    return True, G

  vis = set()
  q = set()
  for i in range(M):
    for j in range(N):
      if G[i][j] == '^':
        q.add((i, j))

  def check(i, j):
    cnt = 0
    for x, y in dirs:
      if 0 <= i + x < M and 0 <= j + y < N:
        if G[i + x][j + y] != '#':
          cnt += 1
    return cnt >= 2

  while q:
    next_q = set()
    for i, j in q:
      for x, y in dirs:
        if 0 <= i + x < M and 0 <= j + y < N:
          if G[i + x][j + y] == '.' and check(i + x, j + y):
            vis.add((i + x, j + y))
            G[i + x][j + y] = '^'
            next_q.add((i + x, j + y))
    q = next_q

  for i in range(M):
    for j in range(N):
      if G[i][j] == '^':
        if not check(i, j):
          return False, None

  return True, G

T = int(input())
for case_num in range(T):
    M, N = get_ints()
    G = []
    for _ in range(M):
      G.append(list(input().rstrip()))
    valid, res = solve(M, N, G)

    if not valid:
      print("Case #{}: Impossible".format(case_num + 1))
    else:
      print("Case #{}: Possible".format(case_num + 1))
      for r in res:
        print(('').join(r))
