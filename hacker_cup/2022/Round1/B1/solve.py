from collections import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

MOD = 10 ** 9 + 7

def solve(tree, well):
  N, M = len(tree), len(well)
  res = 0
  for i in range(N):
    for j in range(M):
      diff = abs(tree[i] - well[j])
      res += pow(diff, 2, MOD)
  return res % MOD

def get():
  X, Y = [], []
  N = int(input())
  for _ in range(N):
    x, y = get_ints()
    X.append(x)
    Y.append(y)
  return X, Y

T = int(input())
for case_num in range(T):
  tree_x, tree_y = get()
  well_x, well_y = get()
  ans = (solve(tree_x, well_x) + solve(tree_y, well_y)) % MOD
  print("Case #{}: {}".format(case_num + 1, ans))
