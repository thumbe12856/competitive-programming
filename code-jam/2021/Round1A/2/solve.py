def solve(cards, upper, lower):
    ans = 0
    for n in range(upper, lower - 1, -1):
        ori_n = n
        idx = 0
        used = 0
        while idx < len(cards):
            num, max_cnt = cards[idx]
            cnt = 0
            while n % num == 0 and cnt < max_cnt:
                cnt += 1
                n //= num
                used += num
            idx += 1

        if n == 1 and upper - used == ori_n:
            ans = ori_n
            break

    return ans

T = int(input())
for case_num in range(T):
    N = int(input())
    cards = []
    upper = 0
    for _ in range(N):
        num, n = list(map(int, input().split()))
        cards.append((num, n))
        upper += num * n

    cards.sort()
    # 30000 comes from that there are at most 60 cards in the multipled part,
    # and the maximum number of the prime is smaller than 500.
    # Therefore, 60 * 500 = 30000.
    # 60 cards is because of 2^60 > 10^15, and 10^15 is the maximum number of the plus part.
    lower = max(2, upper - 30000)
    ans = solve(cards, upper, lower)
    print("Case #{}: {}".format(case_num + 1, ans))
