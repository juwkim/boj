A, B, C, D = map(int, input().split())
nums = [*map(int, input().split())]
for num in nums:
    print(int(0 < (num % (A+B)) <= A) + int(0 < (num % (C+D)) <= C))