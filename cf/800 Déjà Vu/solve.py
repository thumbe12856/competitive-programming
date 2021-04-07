from collections import Counter

def check(S):
    l, r = 0, len(S) - 1
    while l <= r:
        if S[l] != S[r]:
            return False
        l += 1
        r -= 1
    return True

def solve(S):
    target = "a"
    ans = ""
    cs = Counter(S)
    if len(cs) == 1 and target in cs:
        return ans

    idx = None
    for i in range(len(S)):
        if S[len(S) - 1 - i] != target:
            idx = i
            break

    if idx is not None:
        ans = S[:idx] + target + S[idx:]
    return ans

T = int(input())
for _ in range(T):
    S = input()
    ans = solve(S)
    if ans:
        print("Yes")
        print(ans)
    else:
        print("No")
