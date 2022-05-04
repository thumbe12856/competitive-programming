from math import gcd
from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

class BIT:
    def __init__(self, n):
        self.n = n
        self.total = 0
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        self.update_tree(idx, val)
        self.total += val

    def update_tree(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & (-idx)

    def get(self, idx):
        if idx >= self.n:
            return self.total

        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & (-idx)
        return res


def get_key(f, t):
    return (min(f, t), max(f, t))

def solve(N, G, Road, Q):
    ans = [0] * len(Q)
    sorted_q_idx = sorted(range(len(Q)), key=lambda i: (Q[i][1], Q[i][0]))
    sorted_r_idx = sorted(list(Road.keys()), key=lambda r: Road[r])
    bit = BIT(Q[sorted_q_idx[-1]][1])

    can = defaultdict(int)
    q_idx, r_idx = 0, 0
    last_weight = -1
    while q_idx < len(Q):
        node, weight = Q[sorted_q_idx[q_idx]]
        while last_weight <= weight and r_idx < len(sorted_r_idx):
            key = sorted_r_idx[r_idx]
            curr_weight, cost = Road[key]
            if curr_weight > weight:
                break

            bit.update()

            last_weight = curr_weight
            r_idx += 1

        ans[sorted_q_idx[q_idx]] = can[node]
        q_idx += 1

    return (" ").join(map(str, ans))

T = int(input())
for case_num in range(T):
    N, nq = get_ints()

    Road = defaultdict(set)
    G = defaultdict(set)
    for _ in range(N - 1):
        x, y, l, a = get_ints()
        key = get_key(x, y)
        G[x].add(y)
        G[y].add(x)
        Road[key] = (l, a)

    Q = []
    for _ in range(nq):
        c, w = get_ints()
        Q.append((c, w))

    ans = solve(N, G, Road, Q)
    print("Case #{}: {}".format(case_num + 1, ans))
