import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


T = int(input())
for _ in range(T):
    N, M, K = get_ints()

