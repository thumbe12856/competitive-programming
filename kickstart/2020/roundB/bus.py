import math
N = int(input(""))

def valid(x_day):
	for i in range(len(x_day) - 1):
		if x_day[i] > x_day[i + 1]:
			return False, i

	return True, _

for _ in range(N):
	ans = 0
	n, d = list(map(int, input("").split()))
	x = list(map(int, input("").split()))
	
	x_day = [0] * n
	for i in range(n):
		x_day[i] = d - d % x[i]

	for i in range(n - 2, -1, -1):
		if x_day[i] > x_day[i + 1]:
			times = math.ceil((x_day[i] - x_day[i + 1]) / x[i])
			x_day[i] -= x[i] * times

	ans = x_day[0]
	print("Case #{0}: {1}".format(_ + 1, ans))
