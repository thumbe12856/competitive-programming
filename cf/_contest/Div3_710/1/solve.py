
def solve(R, C, X):
    X -= 1
    i, j = X // C, X % C
    # print(i, j)
    return j * R + i + 1

T = int(input())
for _ in range(T):
    R, C, X = map(int, input().split())
    print(solve(C, R, X))
