
def solve(N, nums):
    ans = [float('inf')] * N
    ans[0] = str(0)

    for i in range(N):
        v = nums[i]
        nums[i] = set([
                min(N - 1, i + 1),
                max(0, i - 1),
                v - 1,
            ])
    d = 0
    q = set([0])
    while q:
        next_q = set()
        d += 1
        for node in q:
            for next_node in nums[node]:
                if ans[next_node] == float('inf'):
                    ans[next_node] = str(d)
                    next_q.add(next_node)
        q = next_q

    return ans

N = int(input())
nums = list(map(int, input().split()))
ans = solve(N, nums)
print((" ").join(ans))
