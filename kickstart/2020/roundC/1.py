N = int(input(""))

def solve(K, data):
	ans = 0
	target = K
	for i in range(len(data)):
		if data[i] == target:
			target -= 1
		elif data[i] == K:
			target = K - 1
		else:
			target = K

		if target == 0:
			target = K
			ans += 1

	return ans

for _ in range(N):
	N, K = list(map(int, input("").split()))
	data = list(map(int, input("").split()))
	ans = solve(K, data)
	
	print("Case #{0}: {1}".format(_ + 1, ans))
