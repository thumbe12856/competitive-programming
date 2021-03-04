import heapq
from collections import defaultdict, deque

incomes = defaultdict(list)
intersect = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
lights = defaultdict(list)
mapping = {}
L = {}
D, I, S, V, F = list(map(int, input().split()))
for _ in range(S):
    src, dst, name, l = input().split()
    L[name] = int(l)
    mapping[name] = (int(src), int(dst))
    incomes[int(dst)].append(name)

vis = set()
max_s = 0
for i in range(V):
    S = input().split()
    src = S[0]
    stree_name = S[1]
    vis.add(stree_name)

    rest = S[2:]
    val = 0
    for r in rest:
        vis.add(r)
        val += L[r]
        intersect[mapping[r][1]][r][0] += L[r] # total rest
        intersect[mapping[r][1]][r][1] += 1    # number of cars
        max_s = max(max_s, intersect[mapping[r][1]][r][1])

ans = defaultdict(list)
for i in range(I):
    if len(intersect[i]) == 0:
        for name in incomes[i]:
            ans[i].append((name, 1))
    else:
        for name in intersect[i]:
            if max_s == intersect[i][name][1]:
                ans[i].append((name, 1))
            else:
                ans[i].append((name, 1))

print(len(ans))
for i in range(I):
    if len(ans[i]) == 0:
        continue
    print(i)
    print(len(ans[i]))
    for name, val in ans[i]:
        print(name, val)
