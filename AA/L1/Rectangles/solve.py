from collections import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, points):
    ans = set()
    points_set = set(points)
    for i in range(N):
        for j in range(i + 1, N, 1):
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = x2, y1
            x4, y4 = x1, y2

            if len(set([
                (x1, y1), (x2, y2),
                (x3, y3), (x4, y4)
            ])) != 4 or (x3, y3) not in points_set\
                or (x4, y4) not in points_set:
                continue

            ans.add(
                tuple(
                    sorted([(x1, y1), (x2, y2), (x3, y3), (x4, y4)])
                )
            )

    return len(ans)

N = int(input())
points = []
for _ in range(N):
    x, y = get_ints()
    points.append((x, y))

print(solve(N, points))
