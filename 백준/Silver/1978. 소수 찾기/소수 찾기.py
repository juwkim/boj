N = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if num == 1:
        N -= 1
    elif num > 3:
        count = 0
        for divisor in range(2, num):
            if num % divisor:
                count += 1
            else:
                break
        if count != num - 2:
            N -= 1
print(N)