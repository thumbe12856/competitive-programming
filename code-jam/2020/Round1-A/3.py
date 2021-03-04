N = int(input(""))

def get_neb_val(direction, i, j, comp):
	x, y = direction[0], direction[1]
	ret = -1
	while 0 <= i + x < len(comp) and 0 <= j + y < len(comp[0]):
		i += x
		j += y
		if comp[i][j] != -1:
			ret = comp[i][j]
			break

	return ret

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for _ in range(N):
	r, c = list(map(int, input("").split()))
	comp = []
	for i in range(r):
		comp.append(list(map(int, input("").split())))

	ans = 0
	while True:
		eleminate = set()

		for i in range(r):
			for j in range(c):
				if comp[i][j] == -1:
					continue

				ans += comp[i][j]

				total_val, cnt = 0, 0
				for d in directions:
					val = get_neb_val(d, i, j, comp)
					if val != -1:
						total_val += val
						cnt += 1

				if cnt > 0:
					if total_val / cnt > comp[i][j]:
						eleminate.add((i, j))

		for x, y in eleminate:
			comp[x][y] = -1

		if len(eleminate) == 0:
			break
	
	print("Case #{0}: {1}".format(_ + 1, ans))
