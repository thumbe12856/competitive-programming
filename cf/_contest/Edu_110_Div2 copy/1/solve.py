from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)

def cal():
    sq_set = set()
    i = 0
    while True:
        j = i ** 2
        if j > 5000:
            break
        sq_set.add(j)
        i += 1

    res = []
    for i in range(0, 51, 1):
        for j in range(0, 51, 1):
            k = i ** 2 + j ** 2
            if k == 0 or k not in sq_set:
                continue
            res.append((i, j))

    return set(res)

vis = cal()

T = int(input())
for _ in range(T):
    x, y = get_ints()
    if x == 0 and y == 0:
        print(0)
    elif (x, y) in vis:
        print(1)
    else:
        print(2)
