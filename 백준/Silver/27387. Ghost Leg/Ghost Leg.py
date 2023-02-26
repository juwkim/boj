n, m = map(int, input().split())
nums = [int(input()) for _ in range(m)][::-1]
for i in range(n):
    cur = i
    for num in nums:
        if num == cur:
            cur -= 1
        elif num == cur + 1:
            cur += 1
    print(cur + 1)