N = int(input(""))

for _ in range(N):
	n_jobs = int(input(""))
	intervals = []
	for i in range(n_jobs):
		from_, to_ = list(map(int, input("").split()))
		intervals.append([from_, to_])

	sorted_idx = sorted(range(n_jobs), key=lambda i: (intervals[i][0], intervals[i][1]))

	now_ac = {
		"C": 0,
		"J": 0
	}

	ans = [""] * n_jobs
	for idx in sorted_idx:
		interval = intervals[idx]
		if interval[0] >= now_ac["C"]:
			now_ac["C"] = interval[1]
			ans[idx] = "C"
		elif interval[0] >= now_ac["J"]:
			now_ac["J"] = interval[1]
			ans[idx] = "J"
		else:
			ans = "IMPOSSIBLE"
			break
	if ans != "IMPOSSIBLE":
		ans = ("").join(ans)

	print("Case #{0}: {1}".format(_ + 1, ans))
