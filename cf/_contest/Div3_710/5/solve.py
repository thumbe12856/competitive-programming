import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    A, B = [0] * N, [0] * N
    last_val = 0
    l_vis, r_vis = set(), set()
    q = []
    l, r = 0, 0
    for i in range(N):
        if nums[i] != last_val:
            A[i] = str(nums[i])
            B[i] = str(nums[i])
            l_vis.add(nums[i])
            r_vis.add(nums[i])
            for j in range(max(1, last_val), nums[i] + 1, 1):
                q.append(j)
                r = len(q) - 1
            last_val = nums[i]
            continue

        last_val = nums[i]
        while q[l] in l_vis:
            l += 1
        A[i] = str(q[l])
        l_vis.add(q[l])

        while q[r] in r_vis:
            r -= 1
        B[i] = str(q[r])
        r_vis.add(q[r])

    return (" ").join(A), (" ").join(B)

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    A, B = solve(N, nums)
    print(A)
    print(B)
