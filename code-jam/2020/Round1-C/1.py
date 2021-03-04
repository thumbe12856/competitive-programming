N = int(input(""))



def all_loc(start_x, start_y, directions):
	locations = [(start_x, start_y)]
	x, y = start_x, start_y
	if abs(x) + abs(y) == 0:
		return 0

	ans = "IMPOSSIBLE"
	for i in range(len(directions)):
		d = directions[i]
		if d == "N":
			y += 1
		elif d == "S":
			y -= 1
		elif d == "E":
			x += 1
		else:
			x -= 1

		need = abs(x) + abs(y)
		if i + 1 >= need:
			ans = i + 1
			break

		# locations.append((x, y))
	
	return ans

def solution(start_x, start_y, directions):
	return all_loc(start_x, start_y, directions)


for _ in range(N):
	ans = 0
	start_x, start_y, directions = input("").split()
	start_x, start_y = int(start_x), int(start_y)

	ans = solution(start_x, start_y, directions)	
	print("Case #{0}: {1}".format(_ + 1, ans))
