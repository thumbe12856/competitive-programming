T = int(input())
for _ in range(T):
    A, B, C, D = map(int, input().split())
    nums = [A, B, C, D]
    nums.sort()
    target = set([nums[-1], nums[-2]])

    winner1 = max(A, B)
    winner2 = max(C, D)

    if winner1 in target and winner2 in target:
        print("YES")
    else:
        print("No")
