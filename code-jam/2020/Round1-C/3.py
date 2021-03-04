import collections
N = int(input(""))

def solution(n, d, A):
	ans = float("inf")
	count = collections.defaultdict(int)
	for a in A:
		count[a] += 1

		if count[a] >= d:
			return 0

	if d == 2:
		return 1
	elif len(A) == 1:
		return d - 1

	idx = sorted(count.keys(), key=lambda k: -count[k])
	size_idx = sorted(count.keys(), key=lambda k: -k)

	for i in range(len(idx)):
		base = idx[i]
		num = count[base]
		for j in range(i + 1, len(idx), 1):
			num += count[idx[j]] * (idx[j] // idx[i])

		new_base = base
		if num >= d:
			new_base = base
		else:
			new_base = (base * num) / d

		temp_ans = 0
		for j in range(i, len(idx), 1):
			if idx[j] % new_base == 0:
				temp_ans += (idx[j] // new_base - 1) * count[idx[j]]
			else:
				temp_ans += (idx[j] // new_base) * count[idx[j]]

			# print(j, idx[j], count[idx[j]], temp_ans)

		ans = min(ans, temp_ans)

	if ans == float("inf"):
		return d - 1
	return ans

for _ in range(N):
	n, d = list(map(int, input("").split()))
	A = list(map(int, input("").split()))
	A.sort()
	ans = solution(n, d, A)
	
	print("Case #{0}: {1}".format(_ + 1, int(ans)))
