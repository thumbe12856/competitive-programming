

def solve(M, S):
    lower = str(10 ** (M - 1))
    if M == 1:
        lower = str(0)
        target = S
    else:
        target = S - 1
    min_val = list(lower)
    idx = len(min_val) - 1
    while target > 9 and idx >= 0:
        target -= 9
        min_val[idx] = 9
        idx -= 1

    if idx >= 0 and target >= 0 and int(min_val[idx]) + target <= 9:
        min_val[idx] = int(min_val[idx]) + target
    else:
        print("-1 -1")
        return

    max_val = [0] * M
    target = S
    idx = 0
    while idx < len(max_val):
        if target > 9:
            max_val[idx] = 9
            target -= 9
        else:
            max_val[idx] = target
            target = 0
            break
        idx += 1

    if target != 0:
        print("-1 -1")
        return

    print(("").join(map(str, min_val)), ("").join(map(str, max_val)))


M, S = map(int, input().split())
solve(M, S)
