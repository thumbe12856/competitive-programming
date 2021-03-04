import collections
import sys

N, f = list(map(int, input("").split()))
scale = 5

def solution(currset, candidate, visited, pos, idx):
	next_idx = collections.defaultdict(list)

	for i in idx:
		print(i * scale + 1 + pos)
		sys.stdout.flush()

		ret = input("")
		if ret == "N":
			exit()

		candidate[ret] -= 1
		next_idx[ret].append(i)

	ret = ""
	for c in candidate:
		if c not in visited and candidate[c] == 1:
			ret = c

	if len(ret) == 0:
		f.write("here")
		exit()
	else:
		return ret, next_idx[ret][:]

def ladder(N):
	ret = 1
	for i in range(2, N + 1):
		ret *= i

	return ret

for _ in range(N):

	ans = ""
	visited = set()
	from_ = scale - 1
	currset = collections.defaultdict(lambda: set(["A", "B", "C", "D", "E"]))
	for i in range(ladder(scale) - 1):
		currset[i]

	idx = list(range(119))

	left = set(["A", "B", "C", "D", "E"])
	for i in range(from_, 0, -1):
		val = ladder(i)
		candidate = {"A": val, "B": val, "C": val, "D": val, "E": val}
		a, idx = solution(currset, candidate, visited, from_ - i, idx)
		left.remove(a)
		visited.add(a)
		ans += a

	for l in left:
		ans += l
	
	print(ans)
	sys.stdout.flush()

	ret = input("")
	if ret == "N":
		exit()

