from collections import defaultdict, deque
from heapq import heappush, heappop

def get_input():
    intersect = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    # duration, intersection, street, car, bonus
    D,I,S,V,F = list(map(int, input().split()))
    # print(D,I,S,V,F)
    street_to_info = dict()
    street_to_name = dict()

    vis = set()
    incoming = dict()
    for i in range(I):
        incoming[i] = list()

    for i in range(S):
        s,e,name,sec=input().split()
        # print(s,e,name)
        s = int(s)
        e = int(e)
        sec = int(sec)
        street_to_info[name] = dict()
        street_to_info[name]['si'] = s
        street_to_info[name]['ei'] = e
        street_to_info[name]['cost'] = sec
        street_to_name[name] = (s,e)
        incoming[e].append(name)
        vis.add(name)

    key = 1
    max_s = 0
    for i in range(V):
        data = input().split()
        for name in data[1:]:
            vis.add(name)
            val = street_to_info[name]['cost']
            e = street_to_info[name]['ei']
            intersect[e][name][0] += val # total rest
            intersect[e][name][1] += 1   # number of cars
            max_s = max(max_s, intersect[e][name][key])

    ans = {}
    # print(len(incoming))
    for i, paths in incoming.items():
        # print(len(paths))

        cnt = 0
        # max_s = 0
        for path in paths:
            max_s = max(max_s, intersect[i][path][key])
            # print(intersect[i][path][key])

        for path in paths:
            if intersect[i][path][1] > 0:
                cnt += 1

        if cnt > 0:
            ans[i] = []
            for path in paths:
                if intersect[i][path][key] > max_s // 3:
                    ans[i].append((path, 2))
                elif intersect[i][path][key] > 0:
                    ans[i].append((path, 1))

    print(len(ans))
    for i in ans:
        print(i)
        print(len(ans[i]))
        for path, val in sorted(ans[i], key=lambda a: intersect[i][a[0]][key], reverse=True):
            print(path, val)

get_input()


