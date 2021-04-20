from collections import Counter
 
def solve(S):
    cs = Counter(S)
    stack = []
    vis = set()
    for i in range(len(S)):
        if S[i] not in vis:
            while stack and \
                stack[-1] < S[i] and \
                cs[stack[-1]] > 0:
                vis.discard(stack.pop())
    
            vis.add(S[i])
            stack.append(S[i])
        cs[S[i]] -= 1

    return ("").join(stack)

T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
