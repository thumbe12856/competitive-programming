from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(K, N, M, A, B):
    a_idx, b_idx = 0, 0
    res = []
    while a_idx < N or b_idx < M:
        if a_idx < N:
            if A[a_idx] == 0:
                res.append("0")
                a_idx += 1
                K += 1
                continue

            else:
                if A[a_idx] <= K:
                    res.append(str(A[a_idx]))
                    a_idx += 1
                    continue

        if b_idx < M:
            if B[b_idx] == 0:
                res.append("0")
                b_idx += 1
                K += 1
                continue

            else:
                if B[b_idx] <= K:
                    res.append(str(B[b_idx]))
                    b_idx += 1
                    continue
        break

    if a_idx == N and b_idx == M:
        return (" ").join(res)
    return -1


T = int(input())
for _ in range(T):
    input()
    K, N, M = get_ints()
    A = get_ints()
    B = get_ints()
    print(solve(K, N, M, A, B))
