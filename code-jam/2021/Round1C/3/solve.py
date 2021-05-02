from functools import lru_cache

def trans1(S):
    ret = ""
    for s in S:
        val = 1 - int(s)
        if val == 0 and not ret:
            continue
        ret += str(val)

    if not ret:
        ret = "0"
    return ret

def trans2(S):
    if S == "0":
        return "0"

    return S + "0"

def solve(S, E):
    if S == E:
        return 0

    valid = False
    vis = set()
    step = 0
    vis.add(S)
    q = set()
    q.add((S, tuple([S])))
    while q:
        next_q = set()
        for s, path in q:
            if s is E or s == E:
                valid = True
                # for p in path:
                #     print(p)
                break

            s1 = trans1(s)
            if s1 not in vis:
                vis.add(s1)
                next_q.add((s1, tuple(list(path) + [s1])))

            s2 = trans2(s)
            if s2 not in vis:
                vis.add(s2)
                next_q.add((s2, tuple(list(path) + [s2])))

        if valid:
            break
        step += 1
        q = next_q
        if step >= 20:
            break

    if valid:
        ans = step
    else:
        ans = "IMPOSSIBLE"
    return ans

def solve2(S, E):
    def dfs(s, vis):
        if s == E:
            return True

        if len(s) > 10:
            return False

        s1, s2 = trans1(s), trans2(s)
        if s1 not in vis:
            vis.add(s1)
            res = dfs(s1, vis)
            if res:
                print(s1)

        if s2 not in vis:
            vis.add(s2)
            res = dfs(s2, vis)
            if res:
                print(s2)

        return False

    dfs(S, set([S]))

T = int(input())
for case_num in range(T):
    S, E = input().split()
    ans = solve(S, E)
    # ans = solve2(S, E)
    if ans == "IMPOSSIBLE":
        print(S, E)
    # print("Case #{}: {}".format(case_num + 1, ans))
