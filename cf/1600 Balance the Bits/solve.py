def solve(N, S):
    ans = []
    if S[0] == "0" or S[-1] == "0":
        return ans

    cnt = 0
    for s in S:
        if s == "1":
            cnt += 1
    if cnt & 1:
        return ans
    if cnt == N:
        s = "(" * (N // 2) + ")" * (N // 2)
        return [s, s]

    k = 0
    turn = 0
    a, b = "", ""
    for i in range(N):
        if S[i] == "1":
            if (k << 1) < cnt:
                a += "("
                b += "("
            else:
                a += ")"
                b += ")"
            k += 1
        else:
            if turn:
                a += "("
                b += ")"
            else:
                a += ")"
                b += "("
            turn = 1 - turn

    ans = [a, b]
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    ans = solve(N, S)
    if ans:
        print("Yes")
        print(ans[0])
        print(ans[1])
    else:
        print("No")
