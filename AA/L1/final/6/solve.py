from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

MOD = 998244353

input()
A = get_ints()
B = get_ints()
def cal(nums):
    ans = 1
    for n in nums:
        ans = (ans * n) % MOD
    return ans

if cal(A) == cal(B):
    print("Yes")
else:
    print("No")
