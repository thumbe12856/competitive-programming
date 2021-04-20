import random
from functools import lru_cache
import math

def pow(x, n, mod):
    if n <= 0:
        return 1

    ans = 1
    while n:
        if n & 1:
            ans *= x
            ans %= mod
        x *= x
        x %= mod
        n >>= 1
    return ans

LIMIT = 10 ** 18 + 20
@lru_cache(None)
def is_prime(n):
    # Theorematum Quorundam ad Numeros PRIMOS Spectantium Demonstratio
    if n in set([2, 3, 5]):
        return True

    for _ in range(10):
        x = random.randint(1, LIMIT) % (n - 4) + 2
        t = pow(x, n - 1, n)
        if t != 1:
            return False

    return True

def solve(N):
    if N == 6:
        return 6

    curr_val = math.ceil(math.sqrt(N))
    if not (curr_val & 1):
        curr_val -= 1

    next_prime = curr_val + 2
    while not is_prime(next_prime):
        next_prime += 2

    while True:
        if is_prime(curr_val):
            if curr_val * next_prime <= N:
                return curr_val * next_prime
            next_prime = curr_val
        curr_val -= 2

T = int(input())
for case_num in range(T):
    N = int(input())
    ans = solve(N)
    print("Case #{}: {}".format(case_num + 1, ans))
