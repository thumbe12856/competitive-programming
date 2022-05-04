import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


MOD = 10 ** 9 + 7
T = int(input())
for _ in range(T):
    x, n = get_ints()
    print(pow(x, n, MOD))
