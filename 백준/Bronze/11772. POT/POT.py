n = int(input())
nums = [int(input()) for _ in range(n)]
print(sum((i//10)**(i%10) for i in nums))