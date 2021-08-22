def solve(N, nums):
    i = 2
    while True:
        valid = True
        for n in nums:
            if n % i == 0:
                valid = False
                break

        if valid:
            return i
        i += 1

N = int(input())
nums = set()
for _ in range(N):
    nums.add(int(input()))

print(solve(N, nums))
