import sys
import collections

B, L, D = input("").split()
B, L, D = int(B), int(L), int(D)
scores = list(map(int, input("").split()))

lib_data = [[] for i in range(L)]
books_to_lib = collections.defaultdict(set)

for idx in range(L):
    books_num, days, ships = input("").split()
    books_num, days, ships = int(books_num), int(days), int(ships)
    books = list(map(int, input("").split()))
    books.sort(key=lambda i: -scores[i])

    lib_data[idx] = [books_num, days, ships, books, sum([scores[b] for b in books])]
    for b in books:
        books_to_lib[b].add(idx)

sorted_key = range(L)
# sorted_key = sorted(range(L), key=lambda i: (-sum([scores[b] for b in lib_data[i][3]]) / (lib_data[i][1] + lib_data[i][0] / lib_data[i][2]))) # for c, d
sorted_key = sorted(sorted_key, key=lambda i: (lib_data[i][1] / (lib_data[i][2] + lib_data[i][0])))

curr_day = 0
lib_record = {}
record_idx = []
all_visited = set()

while curr_day < D and sorted_key:
    curr_lib_idx = sorted_key.pop(0)
    curr_day += lib_data[curr_lib_idx][1]

    if curr_day >= D:
        break

    # all book can be shift
    if (D - curr_day) * lib_data[curr_lib_idx][2] >= lib_data[curr_lib_idx][0]:
        lib_record[curr_lib_idx] = lib_data[curr_lib_idx][3][:]
    else:
        target_day = D - curr_day
        total_book_num = target_day * lib_data[curr_lib_idx][2]
        lib_record[curr_lib_idx] = lib_data[curr_lib_idx][3][:total_book_num]

    # remove book from lib that is shifted
    record_idx.append(curr_lib_idx)
    for b in lib_record[curr_lib_idx]:
        all_visited.add(b)
        for lib_idx in books_to_lib[b]:
            if b in lib_data[curr_lib_idx][3]:
                lib_data[curr_lib_idx][3].remove(b)
                lib_data[curr_lib_idx][4] -= scores[b]

            lib_data[curr_lib_idx][0] = len(lib_data[curr_lib_idx][3])
    
    # sorted_key = sorted(sorted_key, key=lambda i: (-sum([scores[b] for b in lib_data[i][3]]) / (lib_data[i][1] + lib_data[i][0] / lib_data[i][2]))) # for c, d
    # sorted_key = sorted(sorted_key, key=lambda i: (lib_data[i][1], -lib_data[i][4] / lib_data[i][2]))

ans = 0
for b in all_visited:
    ans += scores[b]
# print(len(all_visited))

print(ans)
# print(len(lib_record))
# for lib_idx in record_idx:
#     books_num = len(lib_record[lib_idx])
#     print(lib_idx, books_num)

#     for i in range(books_num):
#         if i + 1 < books_num:
#             print(lib_record[lib_idx][i], end=" ")
#         else:
#             print(lib_record[lib_idx][i])
