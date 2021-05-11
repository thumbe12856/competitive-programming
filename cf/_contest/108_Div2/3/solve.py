from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, classes, ability):
    can = set()
    data = defaultdict(list)
    for i in range(N):
        c = classes[i]
        a = ability[i]
        can.add(c)
        data[c].append(a)

    presum = defaultdict(list)
    for c in data:
        data[c].sort(reverse=True)
        last = 0
        presum[c] = [0] * (len(data[c]))
        for i in range(len(data[c])):
            presum[c][i] = last + data[c][i]
            last = presum[c][i]

    ans = []
    for i in range(1, N + 1, 1):
        total = 0
        del_can = set()
        for c in can:
            val = len(data[c]) % i + 1
            if val > len(data[c]):
                del_can.add(c)
            else:
                total += presum[c][-val]

        for d in del_can:
            can.discard(d)

        ans.append(str(total))

    return (" ").join(ans)

T = int(input())
for _ in range(T):
    N = int(input())
    classes = get_ints()
    ability = get_ints()
    print(solve(N, classes, ability))
