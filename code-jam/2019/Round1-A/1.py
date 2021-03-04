N = int(input(""))

def solution(visited_list, curr_val, target, matrix, x, y):
	if curr_val == target:
		return True, visited_list

	r, c = len(matrix), len(matrix[0])
	for i in range(x + 1, x + r, 1):
		for j in range(y + 1, y + c, 1):
			next_x, next_y = i % r, j % c
			if matrix[next_x][next_y] == 0 and next_x != x and next_y != y and \
				next_x + next_y != x + y and next_x - next_y != x - y:

				matrix[next_x][next_y] = 1
				result, result_list = solution(visited_list + [(next_x, next_y)], curr_val + 1, target, matrix, next_x, next_y)
				if result:
					return result, result_list
				matrix[next_x][next_y] = 0

	return False, _

def start(r, c, matrix, target):
	for i in range(r):
		for j in range(c):
			matrix[i][j] = 1
			result, result_list = solution([(i, j)], 1, target, matrix, i, j)
			if result:
				return result, result_list
			matrix[i][j] = 0

	return False, _

for _ in range(N):
	reverse = False
	r, c = list(map(int, input("").split()))
	if r > c:
		reverse = True
		r, c = c, r
	matrix = [[0 for i in range(c)] for j in range(r)]
	target = r * c

	result, result_list = start(r, c, matrix, target)
	
	if not result:
		print("Case #{0}: {1}".format(_ + 1, "IMPOSSIBLE"))
	else:
		print("Case #{0}: {1}".format(_ + 1, "POSSIBLE"))
		for i, j in result_list:
			if reverse:
				print("{0} {1}".format(j + 1, i + 1))
			else:
				print("{0} {1}".format(i + 1, j + 1))
