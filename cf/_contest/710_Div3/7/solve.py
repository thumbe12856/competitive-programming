from collections import Counter, defaultdict

def solve(S):
    q = []
    vis = {}
    for i in range(len(S)):
        if S[i] not in vis:
            vis[S[i]] = len(q)
            q.append(S[i])
        else:
            idx = vis[S[i]]
            ori_idx = idx

            while idx + 1 < len(q) and q[idx + 1] == "":
                idx += 1

            if idx + 1 < len(q) and q[idx + 1] >= S[i]:
                q[ori_idx] = ""
                vis[S[i]] = len(q)
                q.append(S[i])

    return ("").join(q)

T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
