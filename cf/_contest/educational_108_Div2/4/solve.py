import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

N = int(input())
A = get_ints()
B = get_ints()

total = 0
for i in range(N):
    total += A[i] * B[i]
ans = total

for i in range(N):
    x, y = i - 1, i + 1
    temp_total = total
    while 0 <= x < N and 0 <= y < N:
        temp_total -= (A[x] - A[y]) * (B[x] - B[y])
        ans = max(ans, temp_total)
        x -= 1
        y += 1

    x, y = i, i + 1
    temp_total = total
    while 0 <= x < N and 0 <= y < N:
        temp_total -= (A[x] - A[y]) * (B[x] - B[y])
        ans = max(ans, temp_total)
        x -= 1
        y += 1

print(ans)
