N = int(input(""))
M = 1000000000

def decode_dir(directions):
	ret = ""
	dir, times = [], []
	curr_dir = {
		"N": 0,
		"E": 0,
		"W": 0,
		"S": 0
	}

	for i in range(len(directions)):
		if directions[i] == "(":
			dir.append(curr_dir.copy())
			curr_dir = {
				"N": 0,
				"E": 0,
				"W": 0,
				"S": 0
			}
		elif ord("0") <= ord(directions[i]) <= ord("9"):
			times.append(int(directions[i]))

		elif directions[i] == ")":
			t = times.pop()
			for d in curr_dir:
				curr_dir[d] = curr_dir[d] * t

			prev_dir = dir.pop()
			for d in curr_dir:
				curr_dir[d] += prev_dir[d]
		else:
			curr_dir[directions[i]] += 1

	ret = curr_dir
	return ret

for _ in range(N):
	directions = input("")
	really_dir = decode_dir(directions)
	x, y = 1, 1
	really_dir["W"] %= M
	really_dir["E"] %= M
	really_dir["N"] %= M
	really_dir["S"] %= M
	
	x -= really_dir["W"]
	x += really_dir["E"]
	y -= really_dir["N"]
	y += really_dir["S"]

	if x <= 0:
		x = M + x

	if y <= 0:
		y = M + y
	
	print("Case #{0}: {1} {2}".format(_ + 1, x, y))
