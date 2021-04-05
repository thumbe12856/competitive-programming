from collections import defaultdict

def solve(vis):
    # Sorted the alphabet by their fequency in response
    A = sorted(
        list(vis.keys()),
        key=lambda v: vis[v],
        reverse=True
    )

    # The highest frequency to 1, the second highest to 2, etc.
    ans = ""
    for a in A:
        ans += a
    return ans

T = int(input())
for case_num in range(T):
    U = int(input())

    # Record the leading alphabet in vis to calculated the possibility
    vis = defaultdict(int)

    # Only 10 alphabet will be seen in the queries
    seen = set()

    # Every alphabet has 0~10 candidates
    can = {}
    for i in range(26):
        can[chr(ord("A") + i)] = set([j for j in range(10)])

    # 10000 queries
    for _ in range(10 ** 4):
        _, R = input("").split() # M is not important
        for r in R:
            seen.add(r)

        if len(R) >= 2:
            # Record the leading alphabet in vis to calculated the possibility
            vis[R[0]] += 1

            # The leading alphabet is not possible to be 0
            can[R[0]].discard(0)

    # Only one alphabet is possible to be 0
    zero = ""
    for c in can:
        if c not in seen:
            continue
        if 0 in can[c]:
            zero = c
            break

    ans = zero + solve(vis)
    print("Case #{}: {}".format(case_num + 1, ans))
