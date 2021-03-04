import collections
import sys

def get_candidate(now_s):
	reversed_s = now_s[::-1]
	compliment_s = ("").join([str(1 - int(s)) for s in now_s])
	c_r_s = ("").join([str(1 - int(s)) for s in reversed_s])
	candidate = {
		now_s: "now",
		reversed_s: "reverse",
		compliment_s: "comp", 
		c_r_s: "both"
	}
	return set(candidate), candidate

def find_candidate(start, end, candidate, candidate_dict):
	for i in range(start, end):
		# print("candidate: ", candidate)
		print(i + 1)
		sys.stdout.flush()
		temp_s = input("")
		next_candidate = set()
		while candidate:
			c = candidate.pop()
			if c[i - start] == temp_s:
				next_candidate.add(c)

		candidate = next_candidate.copy()
		if len(candidate) == 1:
			ret = candidate.pop()
			direction = candidate_dict[ret]
			return ret, direction

	return candidate, None

def esab(n):
	if n == 10:
		now_s = ""
		for i in range(10):
			print(i + 1)
			sys.stdout.flush()
			now_s += input("")

		reversed_s = now_s[::-1]
		compliment_s = ("").join([str(1 - int(s)) for s in now_s])
		c_r_s = ("").join([str(1 - int(s)) for s in reversed_s])
		candidate = set([now_s, reversed_s, compliment_s, c_r_s])
		temp_s = ""
		for i in range(10):
			print(i + 1)
			sys.stdout.flush()
			temp_s = input("")
			next_candidate = set()
			while candidate:
				c = candidate.pop()
				if c[i] == temp_s:
					next_candidate.add(c)

			candidate = next_candidate.copy()
			if len(candidate) == 1:
				print(candidate.pop())
				sys.stdout.flush()
				ret = input("")
				if ret == "N":
					exit()
				break

	elif n == 20:
		now_s = ""
		for i in range(5):
			print(i + 1)
			sys.stdout.flush()
			now_s += input("")

		for i in range(15, 20):
			print(i + 1)
			sys.stdout.flush()
			now_s += input("")

		final_candidate = set()
		out_candidate, _ = get_candidate(now_s)

		now_s = ""
		for i in range(5, 15):
			print(i + 1)
			sys.stdout.flush()
			now_s += input("")

		middle_candidate, middle_candidate_dict = get_candidate(now_s)
		middle_s, direciton = find_candidate(5, 15, middle_candidate, middle_candidate_dict)
		if direciton == "now":
			final_candidate = out_candidate
		elif direciton == "reverse":
			for o in out_candidate:
				final_candidate.add(o[::-1])
		elif direciton == "comp":
			for o in out_candidate:
				final_candidate.add(("").join([str(1 - int(s)) for s in o]))
		elif direciton == "both":
			for o in out_candidate:
				r = ("").join([str(1 - int(s)) for s in o])
				final_candidate.add(r[::-1])

		before, direciton = find_candidate(0, 5, final_candidate, collections.defaultdict(str))
		if direciton != None:
			print(before[:5] + middle_s + before[5:])
			sys.stdout.flush()
		else:
			final_candidate = before
			out, direciton = find_candidate(15, 20, final_candidate, collections.defaultdict(str))
			print(out[:5] + middle_s + out[5:])
			sys.stdout.flush()

		ret = input("")
		if ret == "N":
			exit()
	else:
		exit()

N, n = list(map(int, input("").split()))
for case in range(N):
	esab(n)
