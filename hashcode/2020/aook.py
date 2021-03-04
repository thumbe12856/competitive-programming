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
# sorted_key = sorted(sorted_key, key=lambda i: (lib_data[i][1] / (lib_data[i][2] + lib_data[i][0]))) # for f
sorted_key = sorted(sorted_key, key=lambda i: (lib_data[i][1], lib_data[i][1] / (lib_data[i][2] + lib_data[i][0]))) # for f
# sorted_key = sorted(sorted_key, key=lambda i: (lib_data[i][4] / (lib_data[i][1] + lib_data[i][0] / lib_data[i][2])))
# score/(sign_day + len(books)/obj.ship)

curr_day = 0
lib_record = {}
record_idx = []
all_visited = set()
ans = 0
visited = {}

# while curr_day < D and sorted_key:
def helper(sorted_key, idx, curr_day, last_book_set):
    if idx >= len(sorted_key):
        global ans
        
        key = tuple(list(last_book_set))
        if key in visited:
            ans = max(ans, visited[key])
            print("ans: ", ans)
            return visited[key]

        curr_ans = 0
        for b in last_book_set:
            curr_ans += scores[b]
        
        visited[key] = curr_ans
        
        ans = max(ans, curr_ans)
        print("ans: ", ans)
        sys.stdout.flush()
        return curr_ans
    
    curr_max = -1
    for i in range(idx, len(sorted_key)):

        curr_lib_idx = sorted_key[idx]
        c_day = curr_day + lib_data[curr_lib_idx][1]

        if c_day >= D:
            key = tuple(list(last_book_set))
            if key in visited:
                ans = max(ans, visited[key])
                print("ans: ", ans)
                return visited[key]

            curr_ans = 0
            for b in last_book_set:
                curr_ans += scores[b]
            
            visited[key] = curr_ans
            
            ans = max(ans, curr_ans)
            print("ans: ", ans)
            sys.stdout.flush()
            return curr_ans
            
        # all book can be shift
        book_set = set()
        if (D - c_day) * lib_data[curr_lib_idx][2] >= lib_data[curr_lib_idx][0]:
            book_set = set(lib_data[curr_lib_idx][3][:])
        else:
            target_day = D - c_day
            total_book_num = target_day * lib_data[curr_lib_idx][2]
            book_set = set(lib_data[curr_lib_idx][3][:total_book_num])
        
        curr_max = max(curr_max, helper(sorted_key, i + 1, c_day, last_book_set | book_set))
    
    return curr_max
    
print(helper(sorted_key, 0, 0, set()))

    
# ans = 0
# for b in all_visited:
#     ans += scores[b]
# # print(len(all_visited))

# print(ans)
# print(len(lib_record))
# for lib_idx in record_idx:
#     books_num = len(lib_record[lib_idx])
#     print(lib_idx, books_num)

#     for i in range(books_num):
#         if i + 1 < books_num:
#             print(lib_record[lib_idx][i], end=" ")
#         else:
#             print(lib_record[lib_idx][i])
