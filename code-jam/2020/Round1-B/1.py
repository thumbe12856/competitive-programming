N = int(input(""))
limit = 10 ** 9 + 10

def traversal(target_x, target_y, curr_x, curr_y, idx, path, visited):
	p = 1 << idx
	
	if p > limit:
		return False, path

	elif target_x == curr_x and target_y == curr_y:
		return True, path

	elif (target_x != curr_x and abs(target_x - curr_x) < p) or \
		(target_y != curr_y and abs(target_y - curr_y) < p):
		return False, path

	elif (curr_x, curr_y) in visited:
		return False, path

	direction = [
		[curr_x, curr_y + p, "N"], # up
		[curr_x, curr_y - p, "S"], # down
		[curr_x + p, curr_y, "E"], # right
		[curr_x - p, curr_y, "W"]  # left
	]

	visited.add((curr_x, curr_y))
	direction.sort(key=lambda d: (d[0] - target_x) * (d[0] - target_x) + (d[1] - target_y) * (d[1] - target_y))
	for x, y, d in direction:
		ret, temp_p = traversal(target_x, target_y, x, y, idx + 1, path + d, visited)
		if ret:
			return ret, temp_p

	visited.remove((curr_x, curr_y))
	return False, path

for _ in range(N):
	target_x, target_y = list(map(int, input("").split()))
	
	result, ans = traversal(target_x, target_y, 0, 0, 0, "", set())
	if not result:
		ans = "IMPOSSIBLE"

	print("Case #{0}: {1}".format(_ + 1, ans))
