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

for i in range(V):
    S = input().split()
    src = S[0]
    stree_name = S[1]

    rest = S[2:]
    val = 0
    for r in rest:
        val += L[r]

    intersect[mapping[stree_name][1]][stree_name][0] += val # total rest
    intersect[mapping[stree_name][1]][stree_name][1] += 1 # number of cars

ans = defaultdict(list)
for i in range(I):
    if len(intersect[i]) == 0:
        for name in incomes[i]:
            ans[i].append((name, 1))
    else:
        s = 0
        for name in intersect[i]:
            s += intersect[i][name][1]

        for name in intersect[i]:
            ans[i].append((name, max(1, int(D * intersect[i][name][1] / s))))

print(len(ans))
for i in range(I):
    print(i)
    print(len(ans[i]))
    for name, val in ans[i]:
        print(name, val)
