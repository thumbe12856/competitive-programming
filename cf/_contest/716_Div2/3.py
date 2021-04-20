N = int(input())
MOD = N

turn = 0
can = {1: [1]}
for i in range(2, N, 1):
    keys = list(can.keys())
    next_can = can.copy()
    for c in keys:
        if c == 0:
            continue
        next_can[(c * i) % MOD] = can[c] + [i]
    can = next_can

ans = []
max_len = 0
for c in can:
    if c % N == 1:
        if len(can[c]) > len(ans):
            ans = can[c]

print(len(ans))
print((" ").join(map(str, ans)))
