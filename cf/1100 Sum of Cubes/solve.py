from math import sqrt
import time
from functools import lru_cache

T = int(input(''))
s = time.time()
cubes = set()
not_cubes = set()
for _ in range(T):
    n = int(input(''))
    valid = False
    e = n ** (1 / 3)
    ori_r = int(e)
    for i in range(1, int(e / 1.5) + 2, 1):
        val = i ** 3
        cubes.add(val)
        target = n - val
        if target <= 0:
            break
        elif target in cubes:
            valid = True
            break

        l, r = i, ori_r
        while l < r:
            mid = (l + r) // 2
            val = mid ** 3
            cubes.add(val)
            if val == target:
                valid = True
                break
            elif val < target:
                l = mid + 1
            else:
                r = mid

        if l ** 3 == target:
            valid = True
        if valid:
            break

    if valid:
        print("Yes")
    else:
        print("No")

e = time.time()
print(e - s)
