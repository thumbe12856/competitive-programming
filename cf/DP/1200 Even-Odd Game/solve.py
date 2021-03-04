T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    odd, even = [], []
    for n in nums:
        if n & 1:
            odd.append(n)
        else:
            even.append(n)

    odd.sort()
    even.sort()
    a, b = 0, 0
    turn = 0
    while odd or even:
        if not odd:
            v = even.pop()
        elif not even:
            v = odd.pop()
        else:
            if odd[-1] > even[-1]:
                v = odd.pop()
            else:
                v = even.pop()

        if turn == 0 and not (v & 1):
            a += v
        elif turn == 1 and v & 1:
            b += v
        turn = 1 - turn

    if a > b:
        print("Alice")
    elif a < b:
        print("Bob")
    else:
        print("Tie")
