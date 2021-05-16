import math
import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    pos, seats = [], []
    for i in range(N):
        if nums[i] == 1:
            pos.append(i)
        else:
            seats.append(i)

    M = len(pos)
    dp = [[float('inf') for i in range(N)] for j in range(M)]
    dp.append([0] * N)
    for i in range(M):
        for j in range(i, len(seats), 1):
            cost = abs(pos[i] - seats[j])
            dp[i][j] = min(
                dp[i][j - 1],
                dp[i - 1][j - 1] + cost
            )

    return dp[len(pos) - 1][len(seats) - 1]

N = int(input())
nums = get_ints()
print(solve(N, nums))
