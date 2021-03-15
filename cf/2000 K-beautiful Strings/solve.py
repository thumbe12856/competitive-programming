from math import gcd as bltin_gcd

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    if K == 1:
        print(S)
        continue

    elif N % K != 0:
        print(-1)
        continue



