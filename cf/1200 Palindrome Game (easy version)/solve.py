def solve(N, S):
    def check(S):
        N = len(S)
        res, zero = set(), set()
        for i in range((N + 1) // 2):
            if S[i] != S[-(i + 1)]:
                if S[i] == "0":
                    res.add(i)
                if S[-(i + 1)] == "0":
                    res.add(N - 1 - i)
            else:
                if S[i] == "0":
                    zero.add(i)
                if S[-(i + 1)] == "0":
                    zero.add(N - 1 - i)
        return res, zero

    can, zeros = check(S)
    A, B = len(zeros), len(can)
    if N & 1 and S[N // 2] == "0" and len(can) == 0:
        A = 1
        B = len(zeros) - 1

    if A == B:
        return "DRAW"
    elif A < B:
        return "ALICE"
    else:
        return "BOB"

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(solve(N, S))
