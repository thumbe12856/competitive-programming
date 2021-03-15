r = {
    "0": "0",
    "1": "1",
    "2": "5",
    "3": "",
    "4": "",
    "5": "2",
    "6": "",
    "7": "",
    "8": "8",
    "9": "",
}

T = int(input())
for _ in range(T):
    max_H, max_M = map(int, input().split())
    S = input()

    max_s = max_H * max_M
    valid = True

    S = S.replace(":", "")
    s = int(S[0:2]) * max_M + int(S[2:4])
    rS = r[S[3]] + r[S[2]] + r[S[1]] + r[S[0]]
    if len(rS) < 4 or (int(rS[0:2]) >= max_H or int(rS[2:4]) >= max_M):
        valid = False
    else:
        valid = True

    while rS not in can or not valid:
        s += 1
        h = str(s // max_M % max_H)
        m = str(s % max_M)
        if len(h) < 2:
            h = "0" + h
        if len(m) < 2:
            m = "0" + m

        S = h + m
        rS = r[S[3]] + r[S[2]] + r[S[1]] + r[S[0]]
        if len(rS) < 4 or (int(rS[0:2]) >= max_H or int(rS[2:4]) >= max_M):
            valid = False
        else:
            valid = True

    ans = S[0:2] + ":" + S[2:4]

    print(ans)
