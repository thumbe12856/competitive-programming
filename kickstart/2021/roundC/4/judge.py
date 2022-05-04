
my = []
with open("my.out", "r") as f:
    for line in f.readlines():
        my.append(line.strip())

ans = []
with open("test.out", "r") as f:
    for line in f.readlines():
        ans.append(line.strip())

for i in range(len(my)):
    if my[i] != ans[i]:
        print(i)
        break
