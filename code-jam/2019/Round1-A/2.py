import collections

N = int(input(""))

class Node:
	def __init__(val):
		self.val = val
		self.next = []

def build_table(s_table, S):
	curr_table = s_table
	for i in range(len(S)):
		s = S[i]
		curr_table.setdefault(s, collections.defaultdict())
		curr_table = curr_table[s]

	curr_table["*"] = "*"

def find(table):
	if table == "*":
		return 1

	ends = 0
	for key in table:
		ends += find(table[key])

	if ends >= 2:
		ends -= 2

	return ends

for _ in range(N):
	n = int(input(""))
	s_table = collections.defaultdict()
	for i in range(n):
		s = input("")
		build_table(s_table, s[::-1])

	ans = n
	for key in s_table:
		ans -= find(s_table[key])
	print("Case #{0}: {1}".format(_ + 1, ans))
	