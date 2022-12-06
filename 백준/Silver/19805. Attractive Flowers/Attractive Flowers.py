g = lambda: [*map(int, input().split())]

n = int(input())
nums = sorted([num - (num % 2 == 0) for num in g()], reverse=True)
if n % 2 == 0:
    del nums[-1]
print(sum(nums))