N = int(input(""))

def is_valid(cards):
	for i in range(1, len(cards)):
		if cards[i][0] - cards[i - 1][0] == 1 or cards[i][0] == cards[i - 1][0]:
			continue
		else:
			return False

	return True


def traversal(cards, path, visited):
	if is_valid(cards):
		return True, path

	for i in range(1, len(cards)):
		for j in range(1, len(cards)):
			if i + j > len(cards):
				continue
				
			next_card = cards[i:i + j] + cards[:i] + cards[i + j:]
			t_next_card = to_tuple(next_card)

			if t_next_card in visited:
				continue

			visited.add(t_next_card)
			path.append([i, j])
			
			ret, temp_path = traversal(next_card, path, visited)
			if ret:
				return True, temp_path

			path.pop()
			visited.remove(t_next_card)

	return False, path

def to_tuple(cards):
	ret = []
	for x, y in cards:
		ret.append(x)
		ret.append(y)

	return tuple(ret)


for _ in range(N):
	ans = 0
	R, S = list(map(int, input("").split()))
	cards = []
	for i in range(S):
		for j in range(R):
			cards.append((j + 1, i + 1))

	visited = set()
	visited.add(to_tuple(cards))
	ret, ans = traversal(cards, [], visited)

	print("Case #{0}: {1}".format(_ + 1, len(ans)))
	for a, b in ans:
		print("{0} {1}".format(a, b))
