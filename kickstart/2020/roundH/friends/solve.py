from collections import defaultdict

T = int(input(""))

def solve(final_G, S, G, f, t):
    vis = set([f])
    q = set()
    for s in S[f]:
        q.add(s)
        vis.add(s)

    ans = 2
    while q:
        # print(f, t, q)
        next_can = set()
        for node in q:
            # print(node, G[node], target_nodes)
            if t in G[node]:
                return ans

            next_can |= G[node]

        q = set()
        # print(next_can, vis)
        for idx in next_can:
            final_G[(f, idx)] = ans

            if idx in vis:
                continue

            vis.add(idx)
            for s in S[idx]:
                if s in vis:
                    continue
                try:
                    G[s].remove(idx)
                except:
                    pass
                q.add(s)
                vis.add(s)
        ans += 1

    final_G[(f, t)] = float('inf')
    return -1

for t in range(T):
    N, Q = list(map(int, input("").split()))
    S = [""] + input().split()
    G = defaultdict(set)
    final_G = {}
    for i in range(1, N + 1):
        s = S[i]
        for j in range(len(s)):
            G[s[j]].add(i)
    # print(G)

    ans = []
    for _ in range(Q):
        f, e = list(map(int, input("").split()))
        if (f, e) not in final_G:
            ans += [str(solve(final_G, S, G, f, e))]
        else:
            ans += [str(final_G[(f, e)])]
    print("Case #{}: {}".format(t + 1, (' ').join(ans)))
