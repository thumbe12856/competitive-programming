from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(S):
    if len(S) != len(set(S)):
        return "NO"

    vis = {}
    N = len(S)
    for i in range(N):
        vis[ord(S[i]) - ord("a")] = i

    l, r = None, None
    for i in range(N):
        if i not in vis:
            return "NO"

        if i > 0:
            if abs(l - vis[i]) != 1 and abs(r - vis[i]) != 1:
                return "NO"
            l, r = min(l, vis[i]), max(r, vis[i])
        else:
            l, r = vis[i], vis[i]
    return "YES"

T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
