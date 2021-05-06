import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    vis = set()
    valid = True
    last = None
    for s in S:
        if last is not None and s in vis and s != last:
            valid = False
            break
        vis.add(s)
        last = s

    if valid:
        print("Yes")
    else:
        print("No")
