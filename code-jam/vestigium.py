N = int(input(""))
for _ in range(N):
	ans, repeat_r, repeat_c = 0, 0, 0
	n = int(input(""))
	c_visited = [[set(), False] for i in range(n)]
	for i in range(n):
		row = list(map(int, input("").split()))
		r_visited = set()

		r_is_count = False
		for j in range(n):
			val = row[j]
			if i == j:
				ans += val

			if not r_is_count and val in r_visited:
				repeat_r += 1
				r_is_count = True

			if not c_visited[j][1] and val in c_visited[j][0]:
				repeat_c += 1
				c_visited[j][1] = True

			c_visited[j][0].add(val)
			r_visited.add(val)


	print("Case #{0}: {1} {2} {3}".format(_ + 1, ans, repeat_r, repeat_c))
