# arr = [9, 7, 3, 1, -1, -3, -7, -9]
# q = []
# for i in range(len(arr)):
#     diff = 0
#     for j in range(len(arr)):
#         diff += abs(arr[i] - arr[j])
#     q.append(diff)
# print(q)

from collections import Counter
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

T = int(input())
for _ in range(T):
    N = int(input())
    arr = get_ints()
    ca = Counter(arr)
    valid = True
    x = float('inf')
    for c in ca:
        x = min(x, c)
        if (ca[c] & 1) or (c & 1) or ca[c] > 2:
            valid = False
            break

    if not valid:
        print("No")
        continue

    last_c = x
    i = 0
    s = 0
    last_s = 0
    for c in sorted(ca):
        if last_c != c:
            val = (c - last_c) / (i * 2)
            if val != int(val):
                valid = False
                break
            last_s += int(val)
            s += last_s

        last_c = c
        i += 1

        if not valid:
            break

    start = (x // 2 - s) // N
    # print(start, x, s)
    if not valid or start <= 0 or (x // 2 - s) % N != 0:
        print("No")
    else:
        # q = []
        # last_c = x
        # i = 0
        # valid = True
        # for c in sorted(ca):
        #     if c == last_c:
        #         curr = start
        #     else:
        #         curr = q[-1] + (c - last_c) // (i * 2)
        #     last_c = c
        #     q.append(-curr)
        #     q.append(curr)
        #     i += 1
        
        # print(q)
        print("Yes")

    # diff_arr = []
    # for i in range(2 * N):
    #     diff = 0
    #     for j in range(2 * N):
    #         diff += abs(q[i] - q[j])
    #     diff_arr.append(diff)

    # print(sorted(diff_arr))
    # print(sorted(arr))
