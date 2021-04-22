N = int(input())
n = N
idx = 2
vis = set([0])
while idx <= n:
    while n % idx == 0:
        n //= idx
        vis.add(idx)

        for j in range(idx, N, idx):
            vis.add(j)

    idx += 1

MOD = N
turn = 0
can = set()
total = 1
for i in range(2, N, 1):
    if i in vis:
        continue

    total = (total * i) % MOD
    can.add(i)

if total != 1:
    idx = 1
    while total > 1:
        if total % i == 0:
            if i in can:
                can.remove(i)
                total //= i

                if total in can:
                    can.remove(total)
                    total = 1

ans = can
print(len(ans) + 1)
print("1 " + (" ").join(map(str, ans)))
