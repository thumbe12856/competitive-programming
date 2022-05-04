import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

ans = 0
N, M = get_ints()
ranks = get_ints()
user = {}
can = set([i + 1 for i in range(N)])
for i in range(N):
    user[i + 1] = ranks[i]
    if ranks[i] < user[1]:
        can.discard(i + 1)

for _ in range(M):
    data = get_ints()
    for i in range(1, len(data), 2):
        idx, diff = data[i], data[i + 1]
        if idx not in can:
            continue
        user[idx] += diff

    # for idx in check_list:
    #     if user[idx] < user[1]:
    #         can.discard(idx)

    print(can)

print(len(can) - 1)
