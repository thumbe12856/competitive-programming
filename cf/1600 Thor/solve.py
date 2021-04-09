from collections import defaultdict, deque

q = deque()
idx, total = 0, 0
vis = defaultdict(deque)
not_valid = set()
max_x = -1
ans = []

N, Q = map(int, input().split())
for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        q.append((idx, x))
        vis[x].append(idx)
        idx += 1
        total += 1

    elif t == 2:
        while vis[x]:
            # All element in vis[x] should be popped out from q, and will do it later.
            # The index are collected in the not_valid set.
            i = vis[x].pop()
            not_valid.add(i)

            # If the element is expired, then skip it.
            if i <= max_x - 1:
                continue
            total -= 1

    else:
        # Check the element is expired or should be popped out.
        while q and (q[0][0] <= x - 1 or q[0][0] in not_valid):
            j, y = q.popleft()
            if j not in not_valid:
                total -= 1
                vis[y].popleft()

        max_x = max(max_x, x)
    ans.append(str(total))

# Trick: print the answer at the end to avoid TLE
# by keep commnicating with kernel space.
print("\n".join(ans))
