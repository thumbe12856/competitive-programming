T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    last_color = 1
    max_color = 1
    for i in range(1, N):
        if nums[i] == nums[i - 1]:
            last_color += 1
        else:
            last_color = 1
        
        max_color = max(max_color, last_color)

    print(max_color)
