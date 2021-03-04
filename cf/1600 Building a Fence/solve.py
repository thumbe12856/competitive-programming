T = int(input())
for _ in range(T):
    N, h = input().split()
    N, h = int(N), int(h)
    H = list(map(int, input().split()))
    valid = True
    lower, upper = H[0], H[0]
    for i in range(1, N - 1):
        upper = min(H[i] + h - 1, upper + h - 1)
        lower = max(H[i], lower + 1 - h)
        if lower > upper:
            valid = False
            break

    if valid and not (lower - h + 1 <= H[-1] <= upper + h - 1):
        valid = False

    if valid:
        print("Yes")
    else:
        print("No")
