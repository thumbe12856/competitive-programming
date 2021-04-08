from collections import defaultdict
from sys import exit

N = int(input())
vis = defaultdict(lambda: defaultdict(int))
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# target:
#  [same, diff, same, diff, ...]
#  [diff, same, diff, same, ...]
#  [same, diff, same, diff, ...]
#  ...
same_color = None
same, diff = [], []
for idx in range(N * N):
    i, j = idx // N, idx % N
    if not (i & 1):
        if not (j & 1):
            same.append(idx)
        else:
            diff.append(idx)
    else:
        if not (j & 1):
            diff.append(idx)
        else:
            same.append(idx)

for _ in range(N * N):
    response = input()
    if response == "Wrong Answer":
        exit()

    response = int(response)
    can = set([1, 2, 3])
    can.remove(response)

    if not can:
        exit()

    # choose the first same_color
    if same_color is None:
        for c in can:
            same_color = c
            break

    if not diff or (same_color in can and same):
        idx = same.pop()
        x, y = idx // N, idx % N

        # If the response always same_color and the diff element will be empty.
        if same_color not in can:
            for i, j in dirs:
                can.discard(vis[i + x][j + y])

            # Switch same_color to another color.
            # Switch to the max value of the candidate.
            same_color = max(can)
        color = same_color
    else:
        idx = diff.pop()
        x, y = idx // N, idx % N

        # The value of the different color is not important.
        # Try to not reuse the same color of its neighbors.
        for i, j in dirs:
            can.discard(vis[i + x][j + y])
        color = min(can)

    vis[x][y] = color
    print("{} {} {}".format(color, x + 1, y + 1), flush=True)
