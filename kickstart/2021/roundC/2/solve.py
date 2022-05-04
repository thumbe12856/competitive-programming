import math

def solve(G):
    ans = 1
    target = math.ceil(math.sqrt(2 * G))
    tG = G << 1
    for k in range(1, target + 1, 1):
        child = tG - k * (k + 1)
        mom = (k << 1) + 2
        if child >= mom and child % mom == 0:
            ans += 1

    return ans

T = int(input())
for case_num in range(T):
    G = int(input())
    ans = solve(G)
    print("Case #{}: {}".format(case_num + 1, ans))
