from collections import deque
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, A, B, nums):
    K = B - A + 1
    presum = [0]
    for n in nums:
        presum.append(presum[-1] + n)

    ans = float('-inf')
    q = deque()
    for i in range(A, N + 1, 1):
        while q and not (
                A <= (i - q[0][1]) <= B
            ):
            q.popleft()

        while q and q[-1][0] > presum[i - A]:
            q.pop()

        q.append((presum[i - A], i - A))
        ans = max(ans, presum[i] - q[0][0])

    return ans

N, A, B = get_ints()
nums = get_ints()
print(solve(N, A, B, nums))
