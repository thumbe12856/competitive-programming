def find_max_prefix_and_postfix(string, max_prefix, max_postfix):
	temp_prefix, temp_postfix = "", ""
	for i in range(len(string)):
		if string[i] == "*":
			break

		temp_prefix += string[i]

	for i in range(len(string) - 1, -1, -1):
		if string[i] == "*":
			break

		temp_postfix += string[i]
	temp_postfix = temp_postfix[::-1]

	if len(temp_prefix) > len(max_prefix):
		max_prefix = temp_prefix

	if len(temp_postfix) > len(max_postfix):
		max_postfix = temp_postfix

	return max_prefix, max_postfix

def check_prefix(max_prefix, pattern):
	length = min(len(max_prefix), len(pattern))
	ret = True
	for i in range(length):
		if pattern[i] == "*":
			break
		elif max_prefix[i] != pattern[i]:
			ret = False
			break
	return ret

def check_postfix(max_postfix, pattern):
	length = min(len(max_postfix), len(pattern))
	ret = True
	for i in range(1, length + 1):
		if pattern[-i] == "*":
			break
		elif max_postfix[-i] != pattern[-i]:
			ret = False
			break
	return ret

N = int(input(""))

for _ in range(N):
	p_num = int(input(""))
	patterns = []
	max_len, max_idx = -1, -1
	max_prefix, max_postfix = "", ""
	for i in range(p_num):
		patterns.append(input(""))
		max_prefix, max_postfix = find_max_prefix_and_postfix(patterns[i], max_prefix, max_postfix)

	not_exisit = False
	for i in range(p_num):
		if not check_prefix(max_prefix, patterns[i]) or not check_postfix(max_postfix, patterns[i]):
			not_exisit = True
			break

	ans = ""
	if not_exisit:
		ans = "*"
	else:
		ans += max_prefix

		for i in range(p_num):
			for j in range(len(patterns[i])):
				if patterns[i][j] == "*":
					continue
				ans += patterns[i][j]

		ans += max_postfix

	print("Case #{0}: {1}".format(_ + 1, ans))
