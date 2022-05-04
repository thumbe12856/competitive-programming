import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, A):
    B_left, B_right = [], []
    while A:
        n = A.pop()
        if len(B_left) == 0:
            B_left.append(n)
        elif len(B_right) == 0:
            B_right.append(n)
        else:
            if len(B_left) == len(B_right):
                B_right.append(n)
            else:
                B_left.append(n)
    B = B_left + B_right[::-1]

    if len(B) & 1:
        l, r = len(B) // 2, len(B) // 2 + 1
    else:
        l, r = len(B) // 2 - 1, len(B) // 2

    last_c = -1
    k = 0
    while N:
        if l < 0:
            n = B[r]
            r += 1
        elif r >= len(B):
            n = B[l]
            l -= 1
        else:
            if N & 1:
                if l > len(B) - r - 1:
                    n = B[l]
                    l -= 1
                else:
                    n = B[r]
                    r += 1
            else:
                if B[l] <= B[r]:
                    n = B[l]
                    l -= 1
                else:
                    n = B[r]
                    r += 1

        if n < last_c:
            return "No"
        last_c = n
        k += 1
        N -= 1

    return "Yes"


T = int(input())
for _ in range(T):
    N = int(input())
    A = get_ints()
    print(solve(N, A))

