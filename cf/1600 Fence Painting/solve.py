def solve(N, M, A, B, C):
    ans = [str(0)] * M
    need = {}
    C_color_dict = {}
    B_color_dict = {}
    last_idx = [-1] * M
    for i in range(N - 1, -1, -1):
        if B[i] not in B_color_dict:
            B_color_dict[B[i]] = i

        if A[i] != B[i]:
            if B[i] not in need:
                need[B[i]] = []
            need[B[i]].append(i)

    for i in range(M):
        if C[i] not in C_color_dict:
            C_color_dict[C[i]] = 0
        C_color_dict[C[i]] += 1

    for i in range(M):
        idx = -1
        if C[i] in need and len(need[C[i]]):
            idx = need[C[i]].pop()
            ans[i] = str(idx + 1)
            last_idx[i] = idx
            if not need[C[i]]:
                del need[C[i]]

        C_color_dict[C[i]] -= 1
        if C_color_dict[C[i]] == 0:
            del C_color_dict[C[i]]

    if need:
        return False, ""

    for i in range(M):
        if ans[i] == "0":
            if C[i] in B_color_dict:
                idx = B_color_dict[C[i]]
                ans[i] = str(idx + 1)
                last_idx[i] = idx

    for i in range(M - 2, -1, -1):
        if last_idx[i] == -1:
            last_idx[i] = last_idx[i + 1]

    for i in range(M):
        if ans[i] == "0":
            if last_idx[i] == -1:
                return False, ""
            else:
                ans[i] = str(last_idx[i] + 1)

    return True, (" ").join(ans)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    res, ans = solve(N, M, A, B, C)
    if res:
        print("Yes")
        print(ans)
    else:
        print("No")
