import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, B):

    i = 0
    d = {}
    for x in B:
        d[x - i] = d.get(x - i, 0) + x
        i += 1

    return max(d.values())

N = int(input())
B = get_ints()
print(solve(N, B))
