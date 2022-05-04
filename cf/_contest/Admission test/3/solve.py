import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, V, nums):
    ans = []
    def dfs(idx, mask, path):
        nonlocal ans
        if idx == N:
            if mask == V:
                return True
            return False

        for i in range(nums[idx] + 1):
            if dfs(idx + 1, mask ^ i, path + [str(i)]):
                ans.append(path + [str(i)])

    dfs(0, 0, [])
    print(len(ans))
    ans.sort()
    for S in ans:
        print("{}={}".format("^".join(S), V))

N, V = map(int, input().split())
nums = get_ints()
solve(N, V, nums)
