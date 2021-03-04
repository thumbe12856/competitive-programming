N = int(input(""))

pascal = {}
ladder_mem = {0: 1}
def build_pascal(n):
	for r in range(1, n + 1):
		left_val = 1
		for c in range(1, r + 1):
			pascal[(r, c)] = left_val
			left_val = int(left_val * (r - c) / c)

def traversal(target, r, c, curr_val, visited, visited_set):
	if pascal[(r, c)] + curr_val > target:
		return False
	elif (r, c) in visited_set:
		return False
	elif len(visited) >= 500:
		return False
	elif pascal[(r, c)] + curr_val == target:
		visited.append((r, c))
		return True

	curr_val += pascal[(r, c)]
	visited.append((r, c))
	visited_set.add((r, c))

	direction = [(r + 1, c + 1), (r + 1, c)]
	direction.sort(key=lambda d: -pascal[d])
	for d in direction:
		result = traversal(target, d[0], d[1], curr_val, visited, visited_set)
		if result:
			return True
			
	# left
	if c - 1 >= 1:
		result = traversal(target, r, c - 1, curr_val, visited, visited_set)
		if result:
			return True

	# right
	if c + 1 <= r:
		result = traversal(target, r, c + 1, curr_val, visited, visited_set)
		if result:
			return True

	# up
	if r - 1 >= 1 and c <= r - 1:
		result = traversal(target, r - 1, c, curr_val, visited, visited_set)
		if result:
			return True

	# up left
	if r - 1 >= 1 and c - 1 >= 1:
		result = traversal(target, r - 1, c - 1, curr_val, visited, visited_set)
		if result:
			return True
	
	visited.pop()
	visited_set.remove((r, c))
	return False

build_pascal(501)
for _ in range(N):
	target = int(input(""))
	
	print("Case #{0}:".format(_ + 1))
	if target > 10000:
		while True:
			continue
	
	visited = []
	visited_set = set()
	result = traversal(target, 1, 1, 0, visited, visited_set)
	if result:
		for v in visited:
			print("{0} {1}".format(v[0], v[1]))
	else:
		while True:
			continue