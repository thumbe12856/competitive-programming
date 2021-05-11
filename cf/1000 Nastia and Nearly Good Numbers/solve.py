import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(A, B):
    if B == 1:
        print("No")
        return

    x = A * B
    vis = set()
    vis.add(x)
    i = x
    while len(vis) < 2:
        if i % x != 0:
            vis.add(i)
        i += A

    vis.add(x + max(vis))
    print("Yes")
    print((" ").join(map(str, sorted(vis))))

T = int(input())
for _ in range(T):
    A, B = get_ints()
    solve(A, B)
