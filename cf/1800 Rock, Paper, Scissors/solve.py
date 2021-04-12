from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = min(A[0], B[1]) + min(A[1], B[2]) + min(A[2], B[0])

b = float('inf')
order = range(6)
for idxs in permutations(order, 6):
    temp_A = A[:]
    temp_B = B[:]
    for idx in idxs:
        if idx == 0:
            val = min(temp_A[0], temp_B[0])
            temp_A[0] -= val
            temp_B[0] -= val

        elif idx == 1:
            val = min(temp_A[1], temp_B[1])
            temp_A[1] -= val
            temp_B[1] -= val

        elif idx == 2:
            val = min(temp_A[2], temp_B[2])
            temp_A[2] -= val
            temp_B[2] -= val

        elif idx == 3:
            val = min(temp_B[0], temp_A[1])
            temp_A[1] -= val
            temp_B[0] -= val

        elif idx == 4:
            val = min(temp_B[1], temp_A[2])
            temp_A[2] -= val
            temp_B[1] -= val

        elif idx == 5:
            val = min(temp_B[2], temp_A[0])
            temp_A[0] -= val
            temp_B[2] -= val

    res = min(temp_A[0], temp_B[1]) + min(temp_A[1], temp_B[2]) + min(temp_A[2], temp_B[0])
    b = min(res, b)

print(b, a)
