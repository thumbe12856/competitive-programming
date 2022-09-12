from collections import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

def build_table(pat):
    table = [0] * len(pat)
    p = 0
    for i in range(1, len(pat)):
        while p > 0 and pat[p] != pat[i]:
            p = table[p - 1]

        if pat[p] == pat[i]:
            table[i] = p + 1
            p += 1

    return table

def compare(s, pattern, table):
    i, j = 0, 0
    while i < len(pattern) and j < len(s):
        if pattern[i] == s[j]:
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = table[i - 1]

    result = i == len(pattern)
    return j, result


def solve(N, K, nums, pattern):
  sn = set(nums)
  p = set(pattern)
  if sn == p and len(p) == 1:
    return "YES"

  if N == 2:
    if K & 1:
      if nums != pattern:
        return "YES"
      return "NO"
    else:
      if nums != pattern:
        return "NO"
      return "YES"

  if K == 0:
    if nums != pattern:
      return "NO"
    return "YES"

  if nums == pattern:
    if K == 1:
      return "NO"
    return "YES"

  nums += nums
  table = build_table(pattern[:-1])
  idx, result = compare(nums, pattern, table)

  if result:
    return "YES"
  return "NO"

T = int(input())
for case_num in range(T):
    N, K = get_ints()
    nums = get_ints()
    pattern = get_ints()
    print("Case #{}: {}".format(case_num + 1, solve(N, K, nums, pattern)))
