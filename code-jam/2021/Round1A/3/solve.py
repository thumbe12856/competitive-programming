from sys import exit
from itertools import combinations

def solve(Q, data, pos):
    ans = ""
    for score, answer in data:
        if score == Q or len(data) == 1:
            ans = "{} {}/1".format(answer, score)
            return ans
        elif score == 0:
            S = ""
            for idx in range(Q):
                t = answer[idx]
                if t == "T":
                    S += "F"
                else:
                    S += "T"
            ans = "{} {}/1".format(S, score)
            return ans

    can = range(Q)
    score1, answer1 = data[0]
    score2, answer2 = data[1]

    max_s, max_val = "", [0, 0]
    for S in pos:
        val = []
        for score in range(0, Q + 1, 1):
            for idx2s in combinations(can, score):
                temp_s1, temp_s2 = 0, 0
                for i in range(Q):
                    if i in idx2s:
                        if answer1[i] == S[i]:
                            temp_s1 += 1
                        if answer2[i] == S[i]:
                            temp_s2 += 1
                    else:
                        if answer1[i] != S[i]:
                            temp_s1 += 1
                        if answer2[i] != S[i]:
                            temp_s2 += 1

                if temp_s1 == score1 and temp_s2 == score2:
                    val.append(score)
                    # print(S, score, temp_s1, temp_s2, idx2s)

        if len(val) and (max_val[1] == 0 or (sum(val) / len(val) > max_val[0] / max_val[1])):
            max_s = S
            # print(val, S)
            max_val = [sum(val), len(val)]

    i = 2
    while i <= min(max_val[0], max_val[1]):
        if max_val[0] % i == 0 and max_val[1] % i == 0:
            max_val[0] = max_val[0] // i
            max_val[1] = max_val[1] // i
        else:
            i += 1
    ans = "{} {}/{}".format(max_s, max_val[0], max_val[1])
    return ans

def dfs(idx, Q):
    if idx == Q:
        return [""]

    res = []
    ret = dfs(idx + 1, Q)
    for r in ret:
        res += ["T" + r, "F" + r]
    return res

pos = [[]]
for i in range(1, 11, 1):
    pos.append(dfs(0, i))

T = int(input())
for case_num in range(T):
    N, Q = map(int, input().split())
    if Q > 10:
        exit()
    data = []
    for _ in range(N):
        answer, score = input().split()
        score = int(score)
        data.append((score, answer))
    ans = solve(Q, data, pos[Q])
    print("Case #{}: {}".format(case_num + 1, ans))
