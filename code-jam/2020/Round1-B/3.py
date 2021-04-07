def check(cards, idx):
    last_r = -1
    for i in idx:
        r, _ = cards[i]
        if r < last_r:
            return False
        last_r = r
    return True

def trans(cards, idx):
    ret = []
    for i in idx:
        r, _ = cards[i]
        ret.append(r)
    return tuple(ret)

def solve(R, S):
    if R == 1 or S == 1:
        return []

    move = []
    cards = []
    for i in range(S):
        for j in range(R):
            cards.append((j + 1, i + 1))

    idx = list(range(len(cards)))
    q = [[idx, []]]
    vis = set()
    vis.add(trans(cards, idx))
    while q:
        next_q = []
        for curr_idx, curr_moves in q:
            last_idx = len(idx)
            for i in range(len(idx) - 1, -1, -1):
                r, _ = cards[curr_idx[i]]
                if r * S >= i >= (r - 1) * S:
                    last_idx = i
                    continue
                else:
                    break

            for i in range(1, last_idx + 1, 1):
                for j in range(i, last_idx + 1, 1):
                    next_idx = curr_idx[i: j + 1] + curr_idx[:i] + curr_idx[j + 1:]
                    tn = trans(cards, next_idx)
                    if tn in vis:
                        continue

                    next_moves = curr_moves + [(i, j - i + 1)]
                    if check(cards, next_idx):
                        return next_moves

                    vis.add(tn)
                    next_q.append([
                        next_idx, next_moves
                    ])

        q = next_q

    return move

T = int(input())
for case_num in range(T):
    R, S = map(int, input().split())
    move = solve(R, S)
    print("Case #{}: {}".format(case_num + 1, len(move)))
    for x, y in move:
        print(x, y)
