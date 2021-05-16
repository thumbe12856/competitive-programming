from collections import defaultdict, deque
from functools import lru_cache
from heapq import *
from itertools import product, permutations
import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

all_can = defaultdict(list)
LIMIT = 10 ** 6

# for i in range(3, LIMIT // 3 + 1, 1):
#     j = i
#     while j <= LIMIT:
#         all_can[i].append(j)
#         j += i

def dfs(target, can, idx, cnt, curr_val):
    print(cnt, curr_val)

    if curr_val > target:
        return 1

    elif curr_val == target:
        return cnt

    elif idx >= len(can):
        return 1

    elif curr_val != 0 and target % curr_val != 0:
        return 1

    return max(
        dfs(target, can, idx + 1, cnt, curr_val),
        dfs(target, can, idx + 1, cnt + 1, curr_val + can[idx]),
    )

vis = {}
def dfs2(curr_val, last_val, d, path):
    key = (curr_val, last_val)
    if key in vis:
        # print("In")
        return d + vis[key]

    if curr_val == 0:
        # print("---", path)
        return d

    elif curr_val < 3:
        vis[key] = float('-inf')
        return float('-inf')

    max_res = 1
    curr = last_val * 2
    for i in range(curr, curr_val + 1, last_val):
        if curr_val % i != 0:
            continue

        res = dfs2(curr_val - i, i, d + 1, path + [i])
        max_res = max(max_res, res)

    vis[key] = max_res - d
    return max_res

def solve(N):
    ans = 1
    for i in range(3, N // 3 + 1, 1):
    # for i in range(N // 3, 2, -1):
        if N % i != 0:
            continue

        # print(i)
        # print(i, flush=True)
        vis = {}
        res = dfs2(N - i, i, 1, [i])
        ans = max(res, ans)
        # print(i, res, flush=True)
        # if res != 1:
        #     return res

    return ans

T = int(input())
for case_num in range(T):
    N = int(input())

    ans = solve(N)
    print("Case #{}: {}".format(case_num + 1, ans))

# for N in range(3, 25):
#     print(N, (N - 2) * 180 / N)
