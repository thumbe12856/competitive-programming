N = int(input(""))

def find_max(min_list, max_list):
	ans_idx = 0
	min_idx, max_idx = 0, 0
	while max_idx < len(max_list) and max_list[max_idx] < min_list[min_idx]:
		max_idx += 1

	# print(min_list, max_list)
	max_val = -1
	while min_idx < len(min_list) and max_idx < len(max_list):
		if min_list[min_idx] <= max_list[max_idx]:
			temp_val = min_idx + len(max_list) - 1 - max_idx
		else:
			min_idx = len(min_list) - 1
			temp_val = min_idx

		if max_val < temp_val:
			max_val = temp_val
			ans_idx = min_idx

		# print(temp_val, max_val, min_idx, len(max_list), max_idx)

		min_idx += 1
		if min_idx >= len(min_list):
			break

		while max_idx < len(max_list) and max_list[max_idx] < min_list[min_idx]:
			max_idx += 1

		if max_idx >= len(max_list):
			max_idx -= 1

	return min_list[ans_idx]

for _ in range(N):
	P, Q = list(map(int, input("").split()))
	min_x, min_y, max_x, max_y = [0], [0], [Q], [Q]
	for i in range(P):
		x, y, d = input("").split()
		x = int(x)
		y = int(y)
		if d == "N":
			min_y.append(y + 1)
		elif d == "S":
			max_y.append(y - 1)
		elif d == "E":
			min_x.append(x + 1)
		elif d == "W":
			max_x.append(x - 1)

	max_x.sort()
	max_y.sort()
	min_x.sort()
	min_y.sort()

	# print(min_x, max_x, min_y, max_y)
	x = find_max(min_x, max_x)
	y = find_max(min_y, max_y)
	print("Case #{0}: {1} {2}".format(_ + 1, x, y))


