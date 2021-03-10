N = int(input())
garland = list(input())
ans = 0
for i in range(1, N, 1):
    if garland[i] == garland[i - 1]:
        garland[i] = (set("RGB") - set(garland[i: i + 2])).pop()
        ans += 1

print(ans)
print(("").join(garland))
