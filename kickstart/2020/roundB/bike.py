N = int(input(""))

for _ in range(N):

	ans = 0
	n = int(input(""))
	checkpoints = list(map(int, input("").split()))

	for i in range(1, n - 1, 1):
		if checkpoints[i - 1] < checkpoints[i] and checkpoints[i] > checkpoints[i + 1]:
			ans += 1

	print("Case #{0}: {1}".format(_ + 1, ans))
