from collections import Counter
import math

def solve(N):
    nums = [i for i in range(N + 1)]
    cnt = 0
    steps = []

    can = set()
    n = N
    while n > 2:
        can.add(n)
        n = math.ceil(math.sqrt(n))

    for i in range(3, N, 1):
        if i in can:
            continue
        nums[i] = math.ceil(nums[i] / nums[-1])
        cnt += 1
        steps.append((i, N))

    for idx in sorted(can, reverse=True):
        target = math.ceil(math.sqrt(nums[idx]))
        while nums[idx] > 1:
            nums[idx] = math.ceil(nums[idx] / nums[target])
            steps.append((idx, target))

    cn = Counter(nums)
    assert len(cn) == 3
    assert cn[0] == 1
    assert cn[1] == N - 1
    assert cn[2] == 1
    assert cnt <= N + 5

    return steps

T = int(input())
for _ in range(T):
    N = int(input())
    ans = solve(N)
    print(len(ans))
    for x, y in ans:
        print(x, y)
