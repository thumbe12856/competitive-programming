import sys

B, L, D = input("").split()
B, L, D = int(B), int(L), int(D)
scores = list(map(int, input("").split()))

data = []
l_books = {}

for idx in range(L):
    books_num, days, ships = input("").split()
    books_num, days, ships = int(books_num), int(days), int(ships)
    books = list(map(int, input("").split()))
    books.sort(key=lambda i: -scores[i])

    data.append([books_num, days, ships])
    l_books[idx] = books

ans = 0
sorted_idx = sorted(range(L), key=lambda i: (data[i][1], -len(l_books[i])))
ans_Lib = {
    sorted_idx[0]: {
        "id": sorted_idx[0],
        "books": []
    }
}

now_day = data[sorted_idx[0]][1]
candidate = set([sorted_idx.pop(0)])
temp_candidate = set()
lock_day = 0
all_visited = set()

while now_day < D:
    if lock_day == 0:
        candidate.update(temp_candidate)
        
        if sorted_idx:
            idx = sorted_idx.pop(0)
            lock_day = data[idx][1]
            temp_candidate.add(idx)

    for c_idx in candidate:

        if c_idx not in ans_Lib:
            ans_Lib[c_idx] = {
                "id": c_idx,
                "books": []
            }

        cnt = 0
        visited = set()
        
        for b in l_books[c_idx]:
            if cnt >= data[c_idx][2]:
                break
            
            if b in all_visited:
                visited.add(b)
                continue

            cnt += 1
            all_visited.add(b)
            ans_Lib[c_idx]["books"].append(b)
        
        for v in visited:
            l_books[c_idx].remove(v)

    lock_day -= 1
    now_day += 1

ans = 0
for b in all_visited:
    ans += scores[b]

# print(ans)
# print(len(all_visited))
visited = set()
for l in ans_Lib:
    if len(ans_Lib[l]["books"]) == 0:
        visited.add(l)

for v in visited:
    del ans_Lib[v]

print(len(ans_Lib))

for l in ans_Lib:
    print(ans_Lib[l]["id"], len(ans_Lib[l]["books"]))
    for i in range(len(ans_Lib[l]["books"])):
        if i + 1 < len(ans_Lib[l]["books"]):
            print(ans_Lib[l]["books"][i], end=" ")
        else:
            print(ans_Lib[l]["books"][i])
