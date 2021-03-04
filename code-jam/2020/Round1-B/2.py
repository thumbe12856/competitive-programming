import sys

N, A, B = list(map(int, input("").split()))
limit = 1000000000

for _ in range(N):
	if A != B:
		exit()

	# up
	up_idx = 0
	for i in range(200):
		up_idx = i
		print("{0} {1}".format(0, limit - i))
		sys.stdout.flush()
		result = input("")
		if result == "WRONG":
			exit()
		elif result == "HIT":
			break

	# down
	down_idx = 0
	for i in range(200):
		down_idx = i
		print("{0} {1}".format(0, -limit + i))
		sys.stdout.flush()
		result = input("")
		if result == "WRONG":
			exit()
		elif result == "HIT":
			break

	# left
	left_idx = 0
	for i in range(200):
		left_idx = i
		print("{0} {1}".format(-limit + i, 0))
		sys.stdout.flush()
		result = input("")
		if result == "WRONG":
			exit()
		elif result == "HIT":
			break

	# right
	right_idx = 0
	for i in range(200):
		right_idx = i
		print("{0} {1}".format(limit - i, 0))
		sys.stdout.flush()
		result = input("")
		if result == "WRONG":
			exit()
		elif result == "HIT":
			break

	x = (left_idx - right_idx) // 2
	y = (down_idx - up_idx) // 2
	print("{0} {1}".format(x, y))
	sys.stdout.flush()
	result = input("")
	if result == "CENTER":
		goal = True
		continue
	elif result == "WRONG":
		exit()
		
	# possible_data = [(x, y)]
	# startA = limit - A + 1
	# startB = limit - B + 1
	startA = 7
	startB = 7
	# for i in range(-startA - 1 + x, startA + 2 + x, 1):
	# 	for j in range(-startB - 1 + y, startB + 2 + y, 1):
	# 		possible_data.add((i, j))

	goal = False
	while possible_data and not goal:
		x, y = possible_data.pop(0)
		print("{0} {1}".format(x, y))
		sys.stdout.flush()
		result = input("")
		if result == "CENTER":
			goal = True
			break
		elif result == "WRONG":
			exit()

	if not goal:
		exit()

