def solve(N, S):
    ans = []
    last_c = -1
    cnt = 0
    for i in range(N):
        c = ord(S[i])
        if c > last_c:
            cnt += 1
        else:
            cnt = 1
        last_c = c
        ans.append(str(cnt))
    return (" ").join(ans)

T = int(input())
for case_num in range(T):
    N = int(input())
    S = input()
    ans = solve(N, S)
    print("Case #{}: {}".format(case_num + 1, ans))

