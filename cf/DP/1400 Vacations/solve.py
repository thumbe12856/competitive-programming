from functools import lru_cache

N = int(input())
nums = list(map(int, input().split()))

@lru_cache(None)
def dfs(last_val, idx):
    if idx == N:
        return 0

    max_val = 0
    val = nums[idx]
    if val == 3:
        if last_val != 1:
            max_val = max(max_val, 1 + dfs(1, idx + 1))

        if last_val != 2:
            max_val = max(max_val, 1 + dfs(2, idx + 1))

        max_val = max(max_val, dfs(0, idx + 1))

    elif val == 2:
        if last_val != 2:
            max_val = max(max_val, 1 + dfs(2, idx + 1))
        else:
            max_val = max(max_val, dfs(0, idx + 1))

    elif val == 1:
        if last_val != 1:
            max_val = max(max_val, 1 + dfs(1, idx + 1))
        else:
            max_val = max(max_val, dfs(0, idx + 1))

    else:
        max_val = dfs(0, idx + 1)

    return max_val

ans = N - dfs(-1, 0)
print(ans)

# N = input()
# p,c = 3,0
# for i in list(map(int, input().split())):
#     if i==p and p!=3:
#         i = 0
#     elif i==3 and p!=3:
#         i-=p
#     if i == 0:
#         c+=1
#     p = i
# print(c)
