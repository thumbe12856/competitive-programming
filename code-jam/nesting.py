N = int(input(""))

for _ in range(N):
	S = input("")
	now_level = 0
	ans = ""
	for i in range(len(S)):
		s = int(S[i])

		while s != now_level:
			if now_level < s:
				now_level += 1
				ans += "("
			elif now_level > s:
				now_level -= 1
				ans += ")"
		ans += S[i]

	while now_level != 0:
		now_level -= 1
		ans += ")"

	print("Case #{0}: {1}".format(_ + 1, ans))
